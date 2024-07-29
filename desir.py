import requests
import json

URL = "http://127.0.0.1:8000/deserializer/"

data = {
    'Member_Name' : 'Jack Kallis',
    'Age' : 40,
    'Address' : 'South Africa'
}

json_data = json.dumps(data)

re = requests.post(url=URL, data = json_data)