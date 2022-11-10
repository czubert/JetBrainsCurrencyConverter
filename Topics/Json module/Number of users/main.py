import json

with open('users.json', 'r') as json_users:
    users = json.load(json_users)

print(len(users['users']))
