#!/usr/bin/python3
"""
Script to gather data from a REST API for a given employee ID.
"""

import requests
from sys import argv

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

    # Filtering completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Displaying progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], len(completed_tasks), len(todo_data)))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
