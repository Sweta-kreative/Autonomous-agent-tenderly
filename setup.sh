#!/bin/bash

# Install required Python packages
pip3 install -r requirements.txt

#activate venv
source venv/bin/activate

# Run the agent script
python3 main.py

# Run the unit test script
python3 -m unittest tests.test_unit

# Run the integeration test script
python3 -m unittest tests.test_integration