import requests

if __name__ == '__main__':
    '''
    按照url 直接执行delete 
    返回码是204 无返回内容
    '''
    # resp = requests.delete('http://127.0.0.1:8000/api/cmdb/devices/3/')
    # print('status_code:', resp.status_code)
    # print('resp_text:', resp.text)

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/3/')
    print(resp.status_code)
    print(type(resp.text))
    print(resp.json())
    print(type(resp.json()))