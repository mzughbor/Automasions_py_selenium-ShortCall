
#for x in [0,1,3,"hl",65,56,5,"kl"]:
#    print(x)

import requests
import json

ADDRESS = 'https://api.premiumy.net/v1.0'
API_KEY = 'qXs1XKfgSECBB_vGYWSVvw'
URL = "{address}?api_key={api_key}".format(address=ADDRESS, api_key=API_KEY)
CSV_URL = "{address}/csv?api_key={api_key}".format(address=ADDRESS, api_key=API_KEY)

print(URL)
print(CSV_URL)

### ZNpQYFBPR5aalrckwVPNcA
#  Method - allocation:price_range
response = requests.post(
    url=URL,
    json={
        'jsonrpc': '2.0',
        'method': 'allocation:price_range',
        'params': {
            'target': {
                'trunk_id': 'ZNpQYFBPR5aalrckwVPNcA'
            },
            'pr_key': 208086,
            'numbers': 3
        },
        'id': None
    })

print(json.dumps(response.json()))
