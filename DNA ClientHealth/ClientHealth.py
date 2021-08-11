import requests
import json

def getClientHealth(base_url, headers):    
    
    api_endpoint = '/dna/intent/api/v1/client-health'
    url = base_url + api_endpoint
    querystring = {"timestamp": ""}
    response = requests.get(url=url, headers=headers, params=querystring).json()

    #  print(json.dumps(response, indent=2, sort_keys=True))

    print(
        f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")


    scores = response['response'][0]['scoreDetail']

    for score in scores:
        if score['scoreCategory']['value'] == 'WIRED':
            print(f"Wired Clients: {score['clientCount']}")
            score_values = score['scoreList']
            for score_value in score_values:
                print(
                    f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
        elif score['scoreCategory']['value'] == 'WIRELESS':
            print(f"Wireless Clients: {score['clientCount']}")
            score_values = score['scoreList']
            for score_value in score_values:
                print(
                    f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")