import requests
import json

URL = "http://127.0.0.1:8000/deserializer/"

data = {
    'id' : 2,
    'Member_Name' : 'Jack Kallis',
    'Address' : 'South Africa'
}

json_data = json.dump('data')

re = requests.put(url=URL, data = json_data)