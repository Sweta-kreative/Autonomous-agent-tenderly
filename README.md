# Autonomous-agent-tenderly


This project implements autonomous agents that communicate and interact using Agent Fork blockchain on Tenderly (via Web3.py). 
The agents support behaviors such as message passing, balance checking, and token transfers.

## Features
- **Reactive Message Handling**: Responds to "hello" and "crypto" messages.
- **Proactive Behavior**: Periodically checks ERC-20 token balance and generates random messages.

## Prerequisites
- Python 3.8 or higher
- A Tenderly fork URL
- Testing Agent fork account with ERC-20 tokens
- Send token to target address
- imported to metamask
- explorer url - https://dashboard.tenderly.co/explorer/vnet/09d8c3c4-2760-4eb4-afc3-fe5cced086c1/transactions
- token contract creation url - https://dashboard.tenderly.co/explorer/vnet/09d8c3c4-2760-4eb4-afc3-fe5cced086c1/tx/0x32ca4f5d18542463f251838978310b632670ece9d4e785326aeaf39528018b13

## metamask setup
Network name - Tenderly (AgentFork)
Rpc url -https://virtual.sepolia.rpc.tenderly.co/124b1b15-11a8-454d-8830-afd67e558ce1
Chain Id - 17002
Currency - ETH

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sweta-kreative/Autonomous-agent-tenderly.git
   cd project

chmod +x setup.sh

Command 

# Install required Python packages
pip3 install -r requirements.txt

# Run the agent script
python3 autonomous_agent.py

# Run the unit test script
python3 -m unittest tests.test_unit

# Run the integeration test script
python3 -m unittest tests.test_integration
