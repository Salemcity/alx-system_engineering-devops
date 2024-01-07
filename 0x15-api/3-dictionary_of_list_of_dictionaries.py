#!/usr/bin/python3
"""script that records all tasks from all employees
extended to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API and export to JSON"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    tasks = {}
    for user in users:
        user_id = user.get("id")
        tasks[user_id] = []
        for task in todos:
            if user_id == task.get("userId"):
                tasks[user_id].append({"task": task.get("title"),
                                       "completed": task.get("completed"),
                                       "username": user.get("username")})
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks, jsonfile)
