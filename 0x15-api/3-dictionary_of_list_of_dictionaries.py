#!/usr/bin/python3
""" Uses a REST API, returns information about all tasks
from all employees."""

import json
import requests


if __name__ == "__main__":

    r = requests.get('https://jsonplaceholder.typicode.com/todos')

    data = {}
    for Id in range(1, 11):
        request = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{Id}'
                )
        name = request.json().get('username')

        data[Id] = []
        for task in r.json():
            if task.get('userId') == Id:
                title = task.get('title')
                status = task.get('completed')
                data[Id].append(
                    {'username': name, 'task': title, 'completed': status}
                    )

    with open(f"todo_all_employees.json", 'w') as file:
        json.dump(data, file)
