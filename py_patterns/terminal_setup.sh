#!/bin/bash

# Function to create and activate a virtual environment
create_and_activate_venv() {
	# Check if the virtual environment directory exists
	if [ ! -d ".venv" ]; then
		# Create the virtual environment
		python3 -m venv .venv
		echo "Virtual environment created."
	fi

	# Activate the virtual environment
	source .venv/bin/activate
	echo "Virtual environment activated."
}

# Call the function to create and activate the virtual environment
create_and_activate_venv
