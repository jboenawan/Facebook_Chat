# application token: b0c594ce-9b1d-3796-8dbe-f4b55d7600f6
# iPwnVBEYbRgOswSyn2kTqZq0qcsa:HM3QaC1nnoRbdqJM91UD70gSvnMa
# aVB3blZCRVliUmdPc3dTeW4ya1RxWnEwcWNzYTpITTNRYUMxbm5vUmJkcUpNOTFVRDcwZ1N2bk1hDQo=
# Content-Type: application/x-www-form-urlencoded
# Authorization: Basic basicAuthorizationToken

import requests
import base64
import json
import pprint
import pandas as pd
import datetime


## Enter user's API key, secret, and Stubhub login
app_token = 'b0c594ce-9b1d-3796-8dbe-f4b55d7600f6'
consumer_key = 'iPwnVBEYbRgOswSyn2kTqZq0qcsa'
consumer_secret = 'HM3QaC1nnoRbdqJM91UD70gSvnMa'
stubhub_username = 'theresia.susanto@hotmail.com'
stubhub_password = 'September13!'

combo = consumer_key + ':' + consumer_secret
basic_authorization_token = base64.b64encode(bytes(combo, 'utf-8'))

print(basic_authorization_token)
headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'Basic '+basic_authorization_token.decode('utf-8'),}
body = {
        'grant_type':'password',
        'username':stubhub_username,
        'password':stubhub_password,
        'scope':'PRODUCTION'}


url = 'https://api.stubhub.com/login'
r = requests.post(url, headers=headers, data=body)
token_response = r.json()
access_token = token_response['access_token']
user_GUID = r.headers['X-StubHub-User-GUID']

print(r)
print(r.text)
print(token_response)


# inventory_url = 'https://api.stubhub.com/search/inventory/v2'
# eventid = '9670859'
# data = {'eventid':eventid, 'rows':200}
headers['Authorization'] = 'Bearer ' + access_token
headers['Accept'] = 'application/json'
headers['Accept-Encoding'] = 'application/json'

# inventory = requests.get(inventory_url, headers=headers, params=data)

# info_url = 'https://api.stubhub.com/catalog/events/v2/' + eventid

city = 'New York'
Testing_URL = "https://api.stubhub.com/search/catalog/events/v3?city={city_name}".format(city_name= city)
info = requests.get(Testing_URL, headers=headers)
pprint.pprint(info.json())
# print(info)