#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_info_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todo_list_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    employee_info_json = employee_info_response.json()
    todo_list_json = todo_list_response.json()

    employee_name = employee_info_json.get('name')
    total_todo_count = len(todo_list_json)

    completed_task_count = 0
    for task in todo_list_json:
        if task.get('completed'):
            completed_task_count += 1

    print(f'Employee {employee_name}\
is done with tasks({completed_task_count}/{total_todo_count}):')
    for task in todo_list_json:
        if task.get('completed'):
            task_title = task.get('title')
            print(f'\t {task_title}')
