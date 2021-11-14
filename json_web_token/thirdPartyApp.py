import requests
import json

# URL = "http://127.0.0.1:8000/studentapifunctionbased/"
# URL = "http://127.0.0.1:8000/getToken/"
# URL = "http://127.0.0.1:8000/verifyToken/"
URL = "http://127.0.0.1:8000/refreshToken/"


# def postData():
#     data = {
#         "username":"admin",
#         "password": 'admin',
#     }
#     json_data = json.dumps(data)
#     req = requests.post(URL, data=json_data,headers={
#         "Content-Type":"application/json",
#     })
#     res = req.json()
#     print(res)
# def postData():
#     data = {
#         "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2OTAzMjM1LCJpYXQiOjE2MzY5MDI5MzUsImp0aSI6IjFjMWQ0MmRlYTdmZTQyNWU4OWYxNTEyZmQ5YzkwNjBkIiwidXNlcl9pZCI6MX0.v8mNYoSjCTTqyvRzzZxSFT5Vsu9riVaPJabXsfKD9Xk",
#     }
#     json_data = json.dumps(data)
#     req = requests.post(URL, data=json_data,headers={
#         "Content-Type":"application/json",
#     })
#     print(req.status_code)
#     res = req.json()
#     print(res)


# refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjk4OTMzNSwiaWF0IjoxNjM2OTAyOTM1LCJqdGkiOiI4NDNmZTE3MGMwZDg0M2U2ODMyZDAzNDdhZjBjZjQ0MiIsInVzZXJfaWQiOjF9.490E6fHRh-SFMJit0QPlRQdGldxRfHLfBngoqj_xFQ0"
# data = {
#     "refresh":refresh_token,
# }

# json_data = json.dumps(data)
# req = requests.post(URL, data=json_data,headers={
#     "Content-Type":"application/json",
# })
# print(req.status_code)
# res = req.json()
# print(res)



# json_data = json.dumps(data)
req = requests.get("http://127.0.0.1:8000/studentapiclassbased/",headers={
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2OTA0NzE3LCJpYXQiOjE2MzY5MDI5MzUsImp0aSI6ImMyOGNmY2ExYTI4MTQyOTM4YjhlY2VhZTlmZmY5ZGYwIiwidXNlcl9pZCI6MX0.m7gjmDqNRQrWmsZC4YPmphJNJQB7XKjVloUj050Ls0Q',
    'Content-Type':"application/json"
})
print(req.status_code)
res = req.json()
print(res)

