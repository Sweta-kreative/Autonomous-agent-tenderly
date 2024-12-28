#!/bin/bash

# Exit script on any error
set -e

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating a virtual environment..."
  python3 -m venv venv
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install required Python packages
echo "Installing dependencies from requirements.txt..."
pip3 install -r requirements.txt

# Confirm successful setup
echo "Setup completed successfully. The virtual environment is activated."