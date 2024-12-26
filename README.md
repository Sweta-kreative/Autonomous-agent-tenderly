# Autonomous-agent-tenderly

This project implements autonomous agents that communicate and interact using Agent Fork blockchain on Tenderly (via Web3.py). The agents support behaviors such as message passing, balance checking, and token transfers.

## Features
- **Reactive Message Handling**: Responds to "hello" and "crypto" messages.
- **Proactive Behavior**: Periodically checks ERC-20 token balance and generates random messages.
- **Token Transfer**: Sends tokens from one agent to another based on conditions.

## Prerequisites
- Python 3.8 or higher
- A **Tenderly fork URL**
- Testing Agent fork account with **ERC-20 tokens**
- Token should be sent to the target address
- Imported to **MetaMask** for testing
- Explorer URL for transactions: [Tenderly Explorer]https://virtual.sepolia.rpc.tenderly.co/0cf741fe-a859-4d93-839e-bf1c4df664a3
- Token contract creation URL: [Tenderly Contract]https://dashboard.tenderly.co/Sweta/project/testnet/e66da6c7-bf30-46fc-81e4-fe68d619ac52/tx/sepolia/0xc1a95248bf50c0533f9bf170d1b16a90b3b791bf8608de42ad29416ffa56ef55

## MetaMask Setup
- **Network name**: Tenderly (AgentTestnet)
- **RPC URL**: `https://virtual.sepolia.rpc.tenderly.co/26e92e61-3f15-4e48-9f07-071a0570f165`
- **Currency**: ETH

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sweta-kreative/Autonomous-agent-tenderly.git
   cd Autonomous-agent-tenderly
   ```

2. **Setup Environment**
   ```bash
   chmod +x setup.sh
   ```

3. **Install Required Python Packages**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run the Agent Script**
   ```bash
   python3 autonomous_agent.py
   ```

5. **Run Unit Tests**
   ```bash
   python3 -m unittest tests.test_unit
   ```

6. **Run Integration Tests**
   ```bash
   python3 -m unittest tests.test_integration
   ```
7. **activate venv**
   ```bash
   source venv/bin/activate
   ```
## Project Structure
```
Autonomous-agent-tenderly/
├── autonomous_agent.py          # Main script to run the agents
├── src/
│   ├── agent.py                 # Defines the AutonomousAgent class
│   └── blockchain_utils.py      # Contains utility functions for blockchain interactions
├── tests/
│   ├── test_unit.py             # Unit tests for individual components
│   └── test_integration.py      # Integration tests for the system as a whole
├── setup.sh                     # Script to set up the environment
├── main.py                      # Script to run the project
├── .gitignore                   # Remove sensitive files
├── requirements.txt             # Python package dependencies
└── README.md                    # Project documentation
```

## Notes
- Ensure your **MetaMask** is connected to the correct network (`Tenderly (AgentTestnet)`).
- The agents will communicate via messages, and each agent will periodically check its balance and send a `hello` message.
- The agents will transfer tokens if the balance is sufficient and a `crypto` message is received.

---

This README provides a clear structure and instructions for setting up and using the project, including all necessary configurations and commands.