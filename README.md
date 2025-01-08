
---

# Autonomous-agent-tenderly

This project implements autonomous agents that communicate and interact using the **Agent Fork blockchain** on **Tenderly** (via Web3.py). The agents support behaviors such as message passing, balance checking, and token transfers.

---

## Features
- **Reactive Message Handling**: Responds to `hello` and `crypto` messages.
- **Proactive Behavior**: Periodically checks ERC-20 token balance and generates random messages.
- **Token Transfer**: Sends tokens from one agent to another based on conditions.

---

## Prerequisites
- **Python 3.8 or higher**
- A **Tenderly fork URL**
- Testing Agent fork account with **ERC-20 tokens**
- Token should be sent to the target address and imported into **MetaMask** for testing.
- Explorer URL for transactions: [Tenderly Explorer](https://virtual.sepolia.rpc.tenderly.co/40f6cc2d-0ded-4881-bc47-c6a31e57a9ce)
- Token contract creation URL: [Tenderly Contract](https://dashboard.tenderly.co/explorer/vnet/40f6cc2d-0ded-4881-bc47-c6a31e57a9ce/tx/0x5883fa16870c3bad7fff42e2d046573927488b5f4e7d73311924299a2d20e0e0)

---

## MetaMask Setup
- **Network Name**: Tenderly (AgentTestnet)  
- **RPC URL**: `https://virtual.sepolia.rpc.tenderly.co/eac04090-7ac1-4c20-b640-94504f53eeb2`  
- **Currency**: ETH  

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Sweta-kreative/Autonomous-agent-tenderly.git
cd Autonomous-agent-tenderly
```

---

## Manual Setup

### Step 1: Create and Activate a Virtual Environment
1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   - On **Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

### Step 2: Install Required Python Packages
Install the dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Agent Script
Start the agent by running:
```bash
python main.py
```

### Step 4: Run Tests
- **Unit Tests**:
  ```bash
  python -m unittest tests.test_unit
  ```
- **Integration Tests**:
  ```bash
  python -m unittest tests.test_integration
  ```

---

## Script-based Setup

For an easier setup process, use the provided `setup.sh` script to automate the environment setup.

### Step 1: Download and Run the Setup Script
1. **Ensure the script is executable**:
   ```bash
   chmod +x setup.sh
   ```

2. **Run the setup script**:
   ```bash
   ./setup.sh
   ```

**What `setup.sh` Does:**
- Creates a Python virtual environment.
- Installs all required Python packages from `requirements.txt`.
- Activates the virtual environment.

### Step 2: Run the Agent Script
After the setup script has completed, run the agent script:
```bash
python main.py
```

### Step 3: Run Tests (Optional)
The `test.sh` script simplifies running tests for the project.

1. **Ensure the script is executable**:
   ```bash
   chmod +x test.sh
   ```

2. **Run the tests**:
   ```bash
   ./test.sh
   ```

**What `test.sh` Does:**
- Activates the virtual environment (if not already active).
- Runs unit tests (`tests/test_unit.py`).
- Runs integration tests (`tests/test_integration.py`).

---

## Project Structure
```
Autonomous-agent-tenderly/
├── src/
│   ├── agent.py                 # Defines the AutonomousAgent class
│   └── blockchain_utils.py      # Contains utility functions for blockchain interactions
├── tests/
│   ├── test_unit.py             # Unit tests for individual components
│   └── test_integration.py      # Integration tests for the system as a whole
├── setup.sh                     # Script to set up the environment
├── test.sh                      # Script to run test cases
├── main.py                      # Script to run the project
├── .gitignore                   # Remove sensitive files
├── requirements.txt             # Python package dependencies
└── README.md                    # Project documentation
```

---