#!/usr/bin/python3
""" Uses a REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import csv
import sys
import requests


if __name__ == "__main__":

    Id = int(sys.argv[1])
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{Id}')
    name = r.json().get('name')

    r = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params={'userId': Id}
            )

    data = r.json()

    with open(f"{Id}.csv", 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow([Id, name, row.get('completed'), row.get('title')])
