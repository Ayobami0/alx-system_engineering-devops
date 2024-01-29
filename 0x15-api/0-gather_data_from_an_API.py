#!/usr/bin/python3
"""
Gathers data from an api and displays them in stdout.

This module gathers data from an api using the employee id as a
parameter then displays it to the standard output.
It wont be executed if imported.
"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_name = 'https://jsonplaceholder.typicode.com'

    employee = requests.get('{}/users/{}'.format(
        base_name, employee_id)).json()
    all_tasks = requests.get(
        '{}/users/{}/todos'.format(base_name, employee_id)).json()
    completed_tasks = requests.get(
        '{}/users/{}/todos?completed=true'.format(
            base_name, employee_id)).json()

    print('Employee {} is done with tasks({}/{}):'.format(
        employee.get('name'),
        len(completed_tasks),
        len(all_tasks)),
        *[t.get('title') for t in completed_tasks], sep='\n\t ')
