import requests
if __name__ == '__main__':

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/6/')

    print('status_code:', resp.status_code)
    print('resp_text:', resp.text)
    print('reso_content',resp.content)
    print('reso_encoding',resp.encoding)

    print('resp_func_json:', resp.json())
    with open('file.jpg','wb') as f:
        f.write(r.content)
