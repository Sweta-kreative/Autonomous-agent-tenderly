import queue
import time
import threading
from datetime import datetime

class AutonomousAgent:
    def __init__(self, name, blockchain_utils):
        self.name = name
        self.inbox = queue.Queue()
        self.outbox = queue.Queue()
        self.message_handlers = {}
        self.behaviors = []
        self.running = True
        self.blockchain_utils = blockchain_utils

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
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # print(f"[{timestamp}] {self.name}: Handling message '{message_type}' with content: {content}")
                    self.message_handlers[message_type](content)
            except queue.Empty:
                pass

    def _execute_behaviors(self):
        while self.running:
            for condition, action in self.behaviors:
                if condition():
                    action()
            time.sleep(1)

    def stop(self):
        self.running = False
        self.inbox_thread.join()
        self.behavior_thread.join()

    def get_balance(self):
        balance = self.blockchain_utils.get_balance()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {self.name}: Crypto balance is {balance}")
        return balance
    
    def transfer_token(self, amount):
        tx_hash = self.blockchain_utils.transfer_token(amount)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(f"[{timestamp}] {self.name}: Transaction sent with hash {tx_hash}")
