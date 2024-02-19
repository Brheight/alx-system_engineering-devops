#!/usr/bin/python3
"""
Script to export employee's TODO list data in CSV format.
"""

import requests
import csv
from sys import argv

def export_to_csv(user_id, user_name, tasks, filename):
    """
    Export data to CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([user_id, user_name, str(task['completed']), task['title']])

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

    # Exporting to CSV file
    filename = "{}.csv".format(employee_id)
    export_to_csv(user_data['id'], user_data['username'], todo_data, filename)

    print("CSV file '{}' has been created.".format(filename))
