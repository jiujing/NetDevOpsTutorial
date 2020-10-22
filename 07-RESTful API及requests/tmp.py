import requests
import json
if __name__ == '__main__':

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/2/')
    print(resp.json())

    data = {
        'ip': '192.168.2.11',
    }

    resp = requests.patch('http://127.0.0.1:8000/api/cmdb/devices/2/',
                          data=json.dumps(data),headers={'content-type':'application/json'})
    print('status_code:', resp.status_code)
    print('resp_json:', resp.text)
