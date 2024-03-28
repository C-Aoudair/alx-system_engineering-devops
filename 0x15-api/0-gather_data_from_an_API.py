#!/usr/bin/python3
""" Uses a REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":

    Id = int(sys.argv[1])
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{Id}')
    name = r.json()['name']
    r = requests.get('https://jsonplaceholder.typicode.com/todos')

    numberOfTasks = 0
    completedTasks = []
    for task in r.json():
        if task['userId'] == Id:
            numberOfTasks += 1
            if task['completed']:
                completedTasks.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".format(
        name,
        len(completedTasks),
        numberOfTasks)
        )

    for title in completedTasks:
        print(f"\t{title}")
