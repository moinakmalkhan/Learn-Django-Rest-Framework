import requests
import json

# URL = "http://127.0.0.1:8000/student/"
URL = "http://127.0.0.1:8000/student/6"
def getData(id=None):
    data={}
    if id is not None:
        data={'id':id}
    jdata=json.dumps(data)
    req = requests.get(url=URL,data=jdata)
    data=req.json()
    print(data)
# getData()

def postData(data=None):
    if not data:
        data={
            "name":"Ahmad",
            "roll":108,
            "city":"Narowal"
        }
    req = requests.post(URL,json=data)
    res = req.json()
    print(res)
# postData()
def updateData(data=None):
    if not data:
        data={
            "id": 5,
            "name": "Moin Khan",
            "roll": 1,
            "city": "Lahore"
        }
    json_data=json.dumps(data)
    req = requests.put(URL,data=json_data)
    res = req.json()
    print(res)
# updateData()
def deleteData(data=None):
    if not data:
        data={"id":7}
    json_data=json.dumps(data)
    req = requests.delete(URL,data=json_data)
    res = req.json()
    print(res)
deleteData()

    
