#!/usr/bin/python3
"""
Exports data for a given employee ID to JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        emp_id
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {emp_id: tasks}

    filename = "{}.json".format(emp_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
