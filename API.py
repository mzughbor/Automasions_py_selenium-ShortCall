import requests
import json
import threading
import datetime

ADDRESS = 'https://api.premiumy.net/v1.0'
API_KEY = 'O941dp1FTCOrVX6aJ7fLVQ'
URL = "{address}?api_key={api_key}".format(address=ADDRESS, api_key=API_KEY)
CSV_URL = "{address}/csv?api_key={api_key}".format(address=ADDRESS, api_key=API_KEY)

#  Method - live_call:get_list_by_account_user
response = requests.post(
    url=URL,
    json={
        'jsonrpc': '2.0',
        'method': 'live_call:get_list_by_account_user',
        'params': {},
        'id': "gAzSR4siQOSUuT9hBEJP-g"
    })
print(response.json())

myLiveCalls = []
print(myLiveCalls)

def CheackISLive():
    indecator = 0
    data = response.json()
    if len(data['result']['live_call_list']) == 0:
        print('not yet')
    else:
        if not data['result']['live_call_list']in myLiveCalls:
            indecator += 1
            myLiveCalls.append(data['result']['live_call_list'])
            now = datetime.datetime.now()
            myLiveCalls.append(now.strftime("%Y-%m-%d %H:%M:%S"))
            myLiveCalls.append(indecator)
            print(myLiveCalls)
    threading.Timer(5.0, CheackISLive).start()

CheackISLive()



# when using dumps() >> you'll have data type <class 'str'>
# loads used to get dict type & it's done here build-in
#print(type(data))
#for result in data['result']:
#    print(result)

#print(response_test.json())
#data_test = response_test.json()
#for result in data_test['result']:
#    print(result)
#print(data_test['result']['not_allocated_numbers'][-1])
