"""
utils.py

Utility functions for the CLI Student Organizer System
"""

import json
import os

# File where all student organizer data will be stored
DATA_FILE = "student_data.json"


def load_data():
    """
    Load saved data from JSON file.

    Returns:
        dict: Dictionary containing schedules,
              assignments, grades, and notes.
    """

    # Create default structure if file does not exist
    if not os.path.exists(DATA_FILE):
        return {
            "schedules": [],
            "assignments": [],
            "grades": [],
            "notes": []
        }

    # Read data from JSON file
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("⚠ Error reading data file.")
        return {
            "schedules": [],
            "assignments": [],
            "grades": [],
            "notes": []
        }


def save_data(data):
    """
    Save data into JSON file.

    Args:
        data (dict): Data to save
    """

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def get_valid_input(prompt, data_type=int, valid_options=None):
    """
    Validate user input.

    Args:
        prompt (str): Message shown to user
        data_type (type): Expected data type
        valid_options (list): Allowed values

    Returns:
        Valid user input
    """

    while True:
        try:
            user_input = data_type(input(prompt))

            # Check if input is among valid options
            if valid_options and user_input not in valid_options:
                print("❌ Invalid option. Please try again.")
                continue

            return user_input

        except ValueError:
            print("❌ Invalid input type. Try again.")


def pause():
    """
    Pause screen until user presses Enter.
    """
    input("\nPress Enter to continue...")
