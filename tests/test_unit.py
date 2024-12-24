import os
import unittest
from unittest.mock import MagicMock
from autonomous_agent import AutonomousAgent, ERC20_ABI

WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
SOURCE_ADDRESS = os.getenv("SOURCE_ADDRESS")
TARGET_ADDRESS = os.getenv("TARGET_ADDRESS")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CHAIN_ID = int(os.getenv("CHAIN_ID"))

class TestAutonomousAgent(unittest.TestCase):
    def test_get_balance(self):
        # Used mock Web3 for unit test
        mock_web3 = MagicMock()
        mock_contract = MagicMock()
        mock_web3.eth.contract.return_value = mock_contract

        # Mock balanceOf function
        mock_contract.functions.balanceOf.return_value.call.return_value = 100

        agent = AutonomousAgent("TestAgent")
        agent.web3 = mock_web3
        agent.contract = mock_contract

        balance = agent.get_balance()
        self.assertEqual(balance, 100)

        mock_contract.functions.balanceOf.assert_called_with(agent.address)

        agent.stop() 

if __name__ == "__main__":
    unittest.main()
