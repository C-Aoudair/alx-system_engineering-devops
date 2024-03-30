#!/usr/bin/python3
""" Uses a REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
import requests
import sys


if __name__ == "__main__":

    Id = sys.argv[1]
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{Id}')
    name = r.json().get('username')

    r = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params={'userId': Id}
            )

    data = {Id: []}
    for task in r.json():
        title = task.get('title')
        status = task.get('completed')
        data[Id].append(
                {'task': title, 'completed': status, 'username': name}
                )

    with open(f"{Id}.json", 'w') as file:
        json.dump(data, file)
