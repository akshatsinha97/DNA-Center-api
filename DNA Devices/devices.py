import requests
import json

def getDevices(base_url, headers):

    device_endpoint = "/dna/intent/api/v1/network-device"
    url = base_url + device_endpoint

    devices = requests.get(url=url, headers=headers, verify=False).json()['response']

    # print(json.dumps(devices, indent=2))
    
    for device in devices:
        if device['hostname'] == "spine1.abc.inc":
            dev_id = device['id']
    dev_vlan_endpoint = f"/dna/intent/api/v1/network-device/{dev_id}/vlan"
    url = base_url + dev_vlan_endpoint

    dev_vlans = requests.get(url=url,
                            headers=headers, verify=False).json()['response']

    print(json.dumps(dev_vlans, indent=2))