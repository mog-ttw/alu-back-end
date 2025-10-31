#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress for a given employee ID
using the JSONPlaceholder REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO progress for a given employee ID."""

    # Get employee information
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Handle invalid ID
    if not user_data:
        print("Employee not found.")
        return

    employee_name = user_data.get("name")

    # Get employee's todos
    todos_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id
        )
    )
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count total and completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print progress
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_tasks
        )
    )

    # Print titles of completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
