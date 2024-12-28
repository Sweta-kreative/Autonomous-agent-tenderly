#!/bin/bash

# Exit script on any error
set -e

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
  echo "Error: Virtual environment not found. Please run setup.sh first."
  exit 1
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Run unit tests
echo "Running unit tests..."
python3 -m unittest tests.test_unit

# Run integration tests
echo "Running integration tests..."
python3 -m unittest tests.test_integration

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "All tests completed successfully!"
