import requests

if __name__ == '__main__':
    '''
    api一般传入的是json，所以建议大家传入数据的时候，用json这个字段赋值，requests会做两个处理
    - 自动将数据编程json字符串
    - header中声明这是一个json的请求
    '''
    data = {
        'ip': '192.168.2.10',
        'name': 'bj-a-a01',
        'vendor': 'Cisco',
        'start_u': 1,
        'end_u': 2
    }

    resp = requests.post('http://127.0.0.1:8000/api/cmdb/devices/', json=data)
    # resp = requests.post('http://127.0.0.1:8000/api/cmdb/devices/', data=data)
    print('status_code:', resp.status_code)
    print('resp_json:', resp.json())


    for i in range(30,60):
        data = {
            'ip': '192.168.2.{}'.format(i),
            'name': 'bj-a-a{}'.format(i),
            'vendor': 'Cisco',
            'start_u': 1,
            'end_u': 2
        }
        resp = requests.post('http://127.0.0.1:8000/api/cmdb/devices/', json=data)
        # resp = requests.post('http://127.0.0.1:8000/api/cmdb/devices/', data=data)
        print('status_code:', resp.status_code)
        print('resp_json:', resp.json())