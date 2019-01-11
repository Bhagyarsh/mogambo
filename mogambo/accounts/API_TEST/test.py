import requests
import json


ENDPOINT = "http://127.0.0.1:8000/api/v1/auth/jwt/"
ENDPOINT_REG = "http://127.0.0.1:8000/api/v1/auth/jwt/register"
data = {
    "email": "a.a@gmail.com",
    "password": "bhagyarsh31"
}
token = ''
headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + token
}
r = requests.post(url = ENDPOINT,data=data,headers=headers)
#print(r.json()['token'])
print(r)
print(r.json())

# data={
#     "email": "bhagyarsh20@gmail.com",
#     "firstname": "bhagyarsh",
#     "lastname": "dhumal",
#     "password": "bhagyarsh31",
    
# }
# r = requests.post(url = ENDPOINT_REG,data=data)
# print(r.json())
# print(r)