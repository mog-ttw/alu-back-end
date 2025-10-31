#!/usr/bin/python3
"""
Exports data for a given employee ID to CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        emp_id
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    filename = "{}.csv".format(emp_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
