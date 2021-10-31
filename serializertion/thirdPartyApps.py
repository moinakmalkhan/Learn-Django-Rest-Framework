import requests

data = requests.get("http://127.0.0.1:8000/stuinfo/1/")

print(data)