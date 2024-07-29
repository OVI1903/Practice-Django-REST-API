import requests
import json

URL = "http://127.0.0.1:8000/deserializer/"

data = {
    'id' : 2,
}

json_data = json.dump('data')

re = requests.delete(url=URL, data = json_data)