#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_info_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id))
    todo_list_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id))

    employee_info_json = employee_info_response.json()
    todo_list_json = todo_list_response.json()

    employee_name = employee_info_json.get('name')
    employee_username = employee_info_json.get('username')
    total_tasks = len(todo_list_json)

    completed_tasks = 0
    for task in todo_list_json:
        if task.get('completed'):
            completed_tasks += 1

    task_dicts = []
    for task in todo_list_json:
        task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_username
                }
        task_dicts.append(task_dict)

    all_data = {employee_id: task_dicts}

    with open(f'{employee_id}.json', 'w') as employee_tasks_list:
        json.dump(all_data, employee_tasks_list)
