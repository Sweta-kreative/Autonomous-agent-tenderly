import threading
import queue
import time
import random
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
SOURCE_ADDRESS = os.getenv("SOURCE_ADDRESS")
TARGET_ADDRESS = os.getenv("TARGET_ADDRESS")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CHAIN_ID = int(os.getenv("CHAIN_ID"))

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function",
    },
]

class AutonomousAgent:
    def __init__(self, name):
        self.name = name
        self.inbox = queue.Queue()
        self.outbox = queue.Queue()
        self.message_handlers = {}
        self.behaviors = []
        self.running = True

        # Web3 setup
        self.web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect Agent Fork network")

        self.contract = self.web3.eth.contract(
            address=self.web3.to_checksum_address(CONTRACT_ADDRESS), abi=ERC20_ABI
        )
        self.private_key = PRIVATE_KEY
        self.address = SOURCE_ADDRESS
        self.target_address = TARGET_ADDRESS

        # Start threads
        self.inbox_thread = threading.Thread(target=self._process_inbox)
        self.behavior_thread = threading.Thread(target=self._execute_behaviors)
        self.inbox_thread.start()
        self.behavior_thread.start()

    def register_message_handler(self, message_type, handler):
        self.message_handlers[message_type] = handler

    def register_behavior(self, condition, action):
        self.behaviors.append((condition, action))

    def send_message(self, recipient, message_type, content):
        recipient.inbox.put((message_type, content))

    def emit_message(self, message_type, content):
        self.outbox.put((message_type, content))

    def _process_inbox(self):
        while self.running:
            try:
                message_type, content = self.inbox.get(timeout=0.5)
                if message_type in self.message_handlers:
                    print(f"{self.name}: Handling message of type '{message_type}' with content: {content}")
                    self.message_handlers[message_type](content)
            except queue.Empty:
                pass

    def _execute_behaviors(self):
        while self.running:
            for condition, action in self.behaviors:
                if condition():
                    action()
            time.sleep(0.5)

    def stop(self):
        self.running = False
        self.inbox_thread.join()
        self.behavior_thread.join()

    def get_balance(self):
        balance = self.contract.functions.balanceOf(self.address).call()
        print(f"{self.name}: Balance is {balance}")
        return balance
    
    def transfer_token(self, amount):
        nonce = self.web3.eth.get_transaction_count(self.address)
        
        # Build transaction
        tx = self.contract.functions.transfer(self.web3.to_checksum_address(self.target_address), amount).build_transaction({
            "chainId": CHAIN_ID,
            "gas": 70000,
            "gasPrice": self.web3.to_wei("5", "gwei"),
            "nonce": nonce,
        })

        # Sign the transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        
        # Send raw transaction to blockchain
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.raw_transaction)

        # Print transaction hash
        print(f"{self.name}: Transaction sent with hash {tx_hash.hex()}")

def create_concrete_agent(name):
    agent = AutonomousAgent(name)

    def hello_handler(content):
        print(f"{agent.name}: Received 'hello' message: {content}")

    def crypto_handler(content):
        print(f"{agent.name}: Received 'crypto' message: {content}")
        if agent.get_balance() >= 1:
            agent.transfer_token(1)
        else:
            print(f"{agent.name}: Not enough balance to process crypto message.")

    def generate_random_message():
        words = ["hello", "world", "crypto", "universe", "sky"]
        msg = f"{random.choice(words)} {random.choice(words)}"
        agent.emit_message("random", msg)

    agent.register_message_handler("hello", hello_handler)
    agent.register_message_handler("crypto", crypto_handler)
    agent.register_behavior(lambda: time.time() % 2 < 0.5, generate_random_message)

    return agent
def run_agent(agent, recipient, message_behavior):
    
    try:
        while agent.running:
            # Send messages to the recipient based on the defined behavior
            message_behavior(agent, recipient)

            while not agent.outbox.empty():
                message = agent.outbox.get()
                print(f"{agent.name} emitted message: {message}")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"Shutting down {agent.name}...")
        agent.stop()

if __name__ == "__main__":
    try:
        agent1 = create_concrete_agent("Agent1")
        agent2 = create_concrete_agent("Agent2")

        def agent1_behavior(agent, recipient):
            agent.send_message(recipient, "hello", "Hello from Agent1")

        def agent2_behavior(agent, recipient):
            agent.send_message(recipient, "crypto", "Agent2 needs tokens!")

        thread1 = threading.Thread(target=run_agent, args=(agent1, agent2, agent1_behavior))
        thread2 = threading.Thread(target=run_agent, args=(agent2, agent1, agent2_behavior))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

    except KeyboardInterrupt:
        print("Terminating agents...")
        agent1.stop()
        agent2.stop()
