#!/usr/bin/python3
""" Uses a REST API, returns information about all tasks
from all employees."""

import json
import requests


def main():
    """ the main function"""

    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = r.json()
    data = {}

    for Id in range(1, 11):
        userName = get_username(users.json()[Id - 1])
        data[Id] = get_data(todos, userName, Id)

    with open(f"todo_all_employees.json", 'w') as file:
        json.dump(data, file)


def get_username(data):
    """ return username from dictionary data"""
    return data.get('username')


def get_data(data, name, Id):
    """ return information about a given user from API data"""

    userList = []

    for task in data:
        if task.get('userId') == Id:
            title = task.get('title')
            status = task.get('completed')
            userList.append(
                    {'username': name, 'task': title, 'completed': status}
                    )

    return userList


if __name__ == "__main__":
    main()
