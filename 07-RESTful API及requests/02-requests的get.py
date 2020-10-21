import requests

if __name__ == '__main__':
    '''
    requests模块直接调用方法
    status_code是状态码 int类型的
    text 是返回的文本 字符串类型的
    json()是一个函数，会将text loads 转成python对象
    content是二进制的返回对象，处理一些图片的时候可以用到
    '''

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/')
    print('status_code:', resp.status_code)
    print('resp_json', resp.json())
    print('resp_text_in_str:', resp.text)
    print('resp_content_in_bytes', resp.content)

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/?page=2&page_size=5')
    print('status_code:', resp.status_code)
    print('resp_json', resp.json())

    params = {
        'page': 2,
        'page_size': 5
    }
    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/',params=params)
    print('status_code:', resp.status_code)
    print('resp_json', resp.json())

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/2')
    print('status_code:', resp.status_code)
    print('resp_json', resp.json())

    resp = requests.get('http://127.0.0.1:8000/api/cmdb/devices/?id=3')
    print('status_code:', resp.status_code)
    print('resp_json', resp.json())
