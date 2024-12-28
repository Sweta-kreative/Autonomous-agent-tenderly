import os
import unittest
from unittest.mock import MagicMock
from src.agent import AutonomousAgent

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
