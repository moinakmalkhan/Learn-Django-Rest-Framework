import requests
import json

URL = "http://127.0.0.1:8000/sutdentModelApi/"


data = {
    "username": "admin",
    "password": "admin"
}
json_data = json.dumps(data)
req = requests.get(URL, data=json_data,headers={
    'Content-Type':"application/json",
    'Authorization': 'Token d6b688ca660b1aa95fc3197cab0cf423406a979b'
})
res = req.json()
print(res)

# URL = "http://127.0.0.1:8000/getToken/"


# data = {
#     "username": "admin",
#     "password": "admin"
# }
# json_data = json.dumps(data)
# req = requests.post(URL, data=json_data,headers={
#     'Content-Type':"application/json",
# })
# res = req.json()
# print(res)
