#!/usr/bin/python3
"""
Exports all employees' tasks to JSON format.
"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]
        data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
