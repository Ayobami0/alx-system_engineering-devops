#!/usr/bin/python3
"""
Gathers data from an api and displays them in stdout.

This module gathers data from an api using the employee id as a
parameter then displays it to the standard output.
It wont be executed if imported.
"""

if __name__ == '__main__':
    import sys

    import requests

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]

    employee = requests.get('{}/users/{}'.format(BASE_URL, employee_id)).json()
    all_tasks = requests.get(
        '{}/users/{}/todos'.format(BASE_URL, employee_id)).json()
    completed_tasks = requests.get(
        '{}/users/{}/todos?completed=true'.format(
            BASE_URL, employee_id)).json()

    print(
        'Employee {} is done with tasks({}/{}):'.format(
            employee.get('name'),
            len(completed_tasks),
            len(all_tasks)),
        *[t.get('title') for t in completed_tasks], sep='\n\t '
    )
