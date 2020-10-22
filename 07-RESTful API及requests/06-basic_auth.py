import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/',
                        auth=HTTPBasicAuth(username='netdevops', password='Admin123!')
                        )
    print('status_code:', resp.status_code)
    print('resp_json', resp.json())
    print('resp_text_in_str:', resp.text)
    print('resp_content_in_bytes', resp.content)