import requests
from requests.auth import HTTPBasicAuth

def get_token(base_url, username, password):

    endpoint = '/dna/system/api/v1/auth/token'
    url = base_url + endpoint 
    token = requests.post(url=url,
     auth=HTTPBasicAuth(username=username,
                        password=password),
       headers={'content-type': 'application/json'},
       verify=False)
       
    data = token.json()
    return data['Token']