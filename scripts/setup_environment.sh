#!/bin/bash

# setup_environment.sh

# Exit immediately if a command exits with a non-zero status
set -e

# Define the Python version and virtual environment name
PYTHON_VERSION="3.9"
VENV_NAME="quantum_ai_env"

# Update package list and install prerequisites
echo "Updating package list..."
sudo apt-get update

echo "Installing Python and pip..."
sudo apt-get install -y python${PYTHON_VERSION} python3-pip python3-venv

# Create a virtual environment
echo "Creating virtual environment: ${VENV_NAME}..."
python${PYTHON_VERSION} -m venv ${VENV_NAME}

# Activate the virtual environment
echo "Activating virtual environment..."
source ${VENV_NAME}/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

echo "Development environment setup complete!"
echo "To activate the virtual environment, run: source ${VENV_NAME}/bin/activate"
