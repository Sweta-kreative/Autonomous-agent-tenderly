import time
import unittest
import threading
from main import create_agent

class TestAgentIntegration(unittest.TestCase):
    def test_agent_communication(self):
        # Create agents
        agent1 = create_agent("Agent1")
        agent2 = create_agent("Agent2")

        def run_agents():
            # Agent1 sends a hello message
            agent1.send_message(agent2, "hello", "Hello from Agent1")

            # Agent2 sends a crypto message
            agent2.send_message(agent1, "crypto", "Agent2 needs tokens!")

            time.sleep(2)

        # Run agents in a separate thread
        thread = threading.Thread(target=run_agents)
        thread.start()
        thread.join()

        self.assertFalse(agent2.inbox.empty())
        message = agent2.inbox.get()
        self.assertEqual(message, ("hello", "Hello from Agent1"))

        self.assertFalse(agent1.inbox.empty())
        message = agent1.inbox.get()
        self.assertEqual(message, ("crypto", "Agent2 needs tokens!"))

        agent1.stop()
        agent2.stop()

if __name__ == "__main__":
    unittest.main()
