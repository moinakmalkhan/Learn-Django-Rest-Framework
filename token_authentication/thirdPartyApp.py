import requests
import json

URL = "http://127.0.0.1:8000/getToken/"


data = {
    "username": "admin",
    "password": "admin"
}
json_data = json.dumps(data)
req = requests.post(URL, data=json_data,headers={
    'Content-Type':"application/json"
})
res = req.json()
print(res)
