import threading
import random
import time
from src.blockchain_utils import BlockchainUtils
from src.agent import AutonomousAgent
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

# Load environment variables
WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
SOURCE_ADDRESS = os.getenv("SOURCE_ADDRESS")
TARGET_ADDRESS = os.getenv("TARGET_ADDRESS")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

hello_interval = 2  # 2 seconds
crypto_interval = 10  # 10 seconds

# Thread-safe time trackers
hello_last_called = threading.Lock()
crypto_last_called = threading.Lock()
hello_last_time = {"time": time.time()}
crypto_last_time = {"time": time.time()}

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

def create_agent(name):
    blockchain_utils = BlockchainUtils(
        WEB3_PROVIDER, PRIVATE_KEY, SOURCE_ADDRESS, TARGET_ADDRESS, CONTRACT_ADDRESS, ERC20_ABI
    )
    agent = AutonomousAgent(name, blockchain_utils)

    def hello_handler(content):
        with hello_last_called:
            current_time = time.time()
            if current_time - hello_last_time["time"] >= hello_interval:
                hello_last_time["time"] = current_time
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] {agent.name}: Received 'hello' message: {content}")

    def crypto_handler(content):
        with crypto_last_called:
            current_time = time.time()
            if current_time - crypto_last_time["time"] >= crypto_interval:
                crypto_last_time["time"] = current_time
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # print(f"[{timestamp}] {agent.name}: Received 'crypto' message: {content}")
                if agent.get_balance() >= 1:
                    agent.transfer_token(1)
                else:
                    print(f"[{timestamp}] {agent.name}: Not enough balance to process crypto message.")

    def generate_random_message():
        words = ["hello", "world", "crypto", "universe", "sky"]
        msg = f"{random.choice(words)} {random.choice(words)}"
        agent.emit_message("random", msg)

    # Register message handlers
    agent.register_message_handler("hello", hello_handler)
    agent.register_message_handler("crypto", crypto_handler)

    # Register behaviors
    agent.register_behavior(lambda: True, generate_random_message)

    return agent

def run_agent(agent, recipient, message_behavior):
    try:
        while agent.running:
            message_behavior(agent, recipient)
            while not agent.outbox.empty():
                message = agent.outbox.get()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # print(f"[{timestamp}] {agent.name} emitted message: {message}")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"Shutting down {agent.name}...")
        agent.stop()

if __name__ == "__main__":
    agent1 = create_agent("Agent1")
    agent2 = create_agent("Agent2")

    def agent1_behavior(agent, recipient):
        agent.send_message(recipient, "hello", "Hello from Agent1")

    def agent2_behavior(agent, recipient):
        agent.send_message(recipient, "crypto", "Agent2 needs tokens!")

    # Create threads to run agent behaviors
    thread1 = threading.Thread(target=run_agent, args=(agent1, agent2, agent1_behavior))
    thread2 = threading.Thread(target=run_agent, args=(agent2, agent1, agent2_behavior))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
