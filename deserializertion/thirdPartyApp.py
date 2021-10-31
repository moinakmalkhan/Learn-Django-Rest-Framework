import requests
import json
url = "http://127.0.0.1:8000/create_student/"
data={
    'name':'Momin Khan',
    'roll':102,
    'city':'Lahore'
}

req = requests.post(url,data=json.dumps(data))
print(req.json())

