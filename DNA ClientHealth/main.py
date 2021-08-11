from auth import get_token
from ClientHealth import getClientHealth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

creds = {'hostname':'https://sandboxdnac.cisco.com',
         'username':'devnetuser',
         'password':'Cisco123!'}

token = get_token(creds['hostname'], creds['username'], creds['password'])
# print(token)

headers = {'content-type': 'application/json',
            'x-auth-token': token}

getClientHealth(creds['hostname'], headers)