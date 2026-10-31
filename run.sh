#!/bin/bash

# Check if venv directory exists
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "[ERROR] Virtual environment not found!"
    echo "Please create it first using: python3 -m venv venv"
    exit 1
fi

# Run the application
python main.py