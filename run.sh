#!/bin/bash

# Check if Xvfb is installed, install if not (run only once, requires sudo)
if ! command -v Xvfb &> /dev/null; then
    echo "Installing Xvfb..."
    sudo apt-get update
    sudo apt-get install -y xvfb
fi

# Check if google-chrome is installed
if ! command -v google-chrome &> /dev/null; then
    echo "Installing Google Chrome..."
    sudo apt-get update
    sudo apt-get install -y google-chrome-stable
fi

# Set display to :99 to avoid conflicts with :0
export DISPLAY=:99

# Check if Xvfb is already running on :99 and clean up if necessary
if [ -f /tmp/.X99-lock ]; then
    echo "Cleaning up existing Xvfb lock file..."
    rm -f /tmp/.X99-lock
    killall Xvfb 2> /dev/null
fi

# Start Xvfb in the background
echo "Starting Xvfb on display :99..."
Xvfb :99 -screen 0 1024x768x24 &

# Wait briefly to ensure Xvfb starts
sleep 3

# Activate the virtual environment (corrected path to .venv)
echo "Activating virtual environment..."
source .venv/bin/activate

# Ensure webdriver-manager and selenium are up-to-date
echo "Updating dependencies..."
pip install --upgrade webdriver-manager selenium

# Run the Python script
echo "Running Snapchat bot..."
python3 src/main.py