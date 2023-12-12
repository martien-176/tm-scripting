# This script will output a list of tasknumbers that you can enter in JOSM search. 
# Run the script with arguments <user_id> <project_id> <token>
# Token must be in between brackets
# author: martien-176

import requests
import sys
import json
import urllib.parse

if len (sys.argv) == 4:
    user_id = sys.argv[1]
    project_id = sys.argv[2]
    token = sys.argv[3]
else:
    print ("Usage: get-tasks <user_id> <project_id> <token>")
    sys.exit()

url = "https://tasking-manager-tm4-production-api.hotosm.org/api/v2/users/" + user_id + "/tasks/?project_id=" + project_id + "&page_size=1000"
headers = {
    'accept': 'application/json',
    'Authorization': token
}

response = requests.get(url, headers=headers)

if response.status_code == requests.codes.ok:
    data = response.json()# Process the response data
else:
    print("Something went wrong")

def extract_task_ids(data):
    tasks = data['tasks']
    task_ids = []

    for task in tasks:
        if 'taskId' in task:
            task_ids.append(task['taskId'])

    return task_ids

task_ids = extract_task_ids(data)

concat_task_id = ""

for number in task_ids:
    concat_task_id += f"taskId={number} OR "

concat_task_id = concat_task_id[:-4]

print()
print(concat_task_id)
print()