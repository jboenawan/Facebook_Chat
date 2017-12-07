import requests 
import base64

app_token = "b0c594ce-9b1d-3796-8dbe-f4b55d7600f6"
consumer_key = "iPwnVBEYbRgOswSyn2kTqZq0qcsa"
consumer_secret = "HM3QaC1nnoRbdqJM91UD70gSvnMa"
stubhub_username = ""
stubhub_password = ""

combo = consumer_key + ":" + consumer_secret
basic_authorization_token = base64.b64encode(combo.envode('utf-8'))

url = 'https://api.stubhub.com/login'
