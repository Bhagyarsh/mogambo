import requests
import base64
import json
import os
img_path = os.path.join(os.getcwd(),"inkscape.jpg")
ENDPOINT_soft = "http://127.0.0.1:8000/api/v1/software/create"
data = {
    "email": "jay@gmail.com",
    "password": "bhagyarsh31"
}
print(json.dumps(data))
token = ''
ENDPOINT = "http://127.0.0.1:8000/api/v1/auth/jwt"
headers = {
    "Content-Type": "application/json"
}
r = requests.post(url = ENDPOINT,data=json.dumps(data),headers=headers)
print(r)
print(r.content)
token = (r.json()['token'])
print(r)
print(data)
data = {
    "name": "inkscape",
    "version": "10",
    "weburl": "https://inkscape.org/",
    "description": "abc",
    "offical": False,
    "total_downloads": 0,
    "verified": False,
    "category":["animations"],
    "ratings": "1",
    "whats_new": "abc",
    "Tag": [1]
    }
with open(img_path,'rb') as icon:
    file_data = {
        "icon":icon,
        "ScreenShot": None
    }
   
    headers = {
        "Authorization" : "JWT "+ token,
    #    "Content-Type":  "multipart/form-data"
    }
    print(json.dumps(data))

    r = requests.post(url =ENDPOINT_soft,files=file_data ,data=(data),headers=headers )
    print(r)
    print(r.json())