#!/usr/bin/python3
"""
Script to export employee's TODO list data in JSON format.
"""

import requests
import json
from sys import argv

def export_to_json(user_id, user_name, tasks, filename):
    """
    Export data to JSON file.
    """
    data = {str(user_id): [{"task": task['title'], "completed": task['completed'], "username": user_name} for task in tasks]}
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # API endpoint URL
    api_url = "https://jsonplaceholder.typicode.com"

    # Fetching user data
    user_response = requests.get("{}/users/{}".format(api_url, employee_id))
    user_data = user_response.json()

    # Fetching user's TODO list
    todo_response = requests.get("{}/todos?userId={}".format(api_url, employee_id))
    todo_data = todo_response.json()

    # Exporting to JSON file
    filename = "{}.json".format(employee_id)
    export_to_json(user_data['id'], user_data['username'], todo_data, filename)

    print("JSON file '{}' has been created.".format(filename))
