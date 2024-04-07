import urllib.request
import json
import sys

def fetch_employee_todo_progress(employee_id):
  """
  Fetches and displays the TODO LIST PROGRESS FOR A GIVBEN EMPLOYEE ID.
  Parameters:
    employee_id (int): THe id of the employee
  """
  try:
    # Fetch employee data
    url = f'https:/jsonplaceholder.typicode.com/users/{employee_id}'
    with urllib.request.urlopen(url) as response:
      employee_data = json.loads(response.read())

    employee_name = employee_data['name']

    # Fetch TODO list for employee
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    with urllib.request.urlopen(todo_url) as response:
      todos = json.loads(response.read())

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    num_done_tasks = len(done_tasks)

    #Display progress
    print(f'Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):')
    for task in done_tasks:
      print(f"\t{task['title']")

