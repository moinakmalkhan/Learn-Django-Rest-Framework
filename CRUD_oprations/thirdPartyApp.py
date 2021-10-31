import requests
import json

# URL = "http://127.0.0.1:8000/studentapifunctionbased/"
URL = "http://127.0.0.1:8000/studentapiclassbased/"
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
            "roll":107,
            "city":"Narowal"
        }
    json_data=json.dumps(data)
    req = requests.post(URL,data=json_data)
    res = req.json()
    print(res)
# postData()
def updateData(data=None):
    if not data:
        data={
            "id":6,
            "city":"Lahore"
        }
    json_data=json.dumps(data)
    req = requests.put(URL,data=json_data)
    res = req.json()
    print(res)
# updateData()
def deleteData(data=None):
    if not data:
        data={"id":8}
    json_data=json.dumps(data)
    req = requests.delete(URL,data=json_data)
    res = req.json()
    print(res)
# deleteData()

    
