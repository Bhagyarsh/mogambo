import requests
import json
BASE = "http://127.0.0.1:8000/"
ENDPOINT_verify   = "http://127.0.0.1:8000/api/v1/auth/jwt/verify"
ENDPOINT = "http://127.0.0.1:8000/api/v1/auth/jwt"
ENDPOINT_REG = "http://127.0.0.1:8000/api/v1/auth/jwt/register"
# data = {
#     "email": "a.a@gmail.com",
#     "password": "bhagyarsh31"
# }
# print(json.dumps(data))
# token = ''
# ENDPOINT = "http://127.0.0.1:8000/api/v1/auth/jwt"
# headers = {
#     "Content-Type": "application/json"
# }
# r = requests.post(url = ENDPOINT,data=data)
# print(r.json()['token'])
# print(r)
# print(data)
# token = (r.json()['token'])
# data ={
#     "token":token+"123"
# }
# r = requests.post(url = ENDPOINT_verify,data=data)
# print(r.json())
data={
    "email": "bhagyarsh@gmail.com",
    "firstname": "bhagyarsh",
    "lastname": "dhumal",
    "password": "bhagyarsh31",
    
}
r = requests.post(url = ENDPOINT_REG,data=data)

print(r)