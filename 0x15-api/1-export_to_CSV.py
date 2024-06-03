#!/usr/bin/python3
""" 1. Input employee ID, output info to CSV file. """

import csv
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

    with open('{}.csv'.format(employee_id), 'w') as employee_tasks_file:
        writer = csv.writer(
                employee_tasks_file, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL)

        for task in todo_list_json:
            task_user_id = task.get('userId')
            task_completed = task.get('completed')
            task_title = task.get('title')

            row_data = [task_user_id, employee_username, task_completed,
                        task_title]
            writer.writerow(row_data)
