import requests

if __name__ == '__main__':
    '''
    put放入的数据必须是全部字段，patch可以只放一部分数据，RESTful中一般会把id放在url后面
    patch可以放入部分字段，这是二者的区别
    实际使用中实际情况实际分析
    
    '''
    data = {
        'ip': '192.168.2.10',
        'name': 'bj-a-a01',
        'vendor': 'Cisco',
        'start_u': 1,
        'end_u': 2
    }

    resp = requests.put('http://127.0.0.1:8000/api/cmdb/devices/2/', json=data)
    print('status_code:', resp.status_code)
    print('resp_json:', resp.text)

    data = {
        'ip': '192.168.2.10',
        'name': 'bj-a-a01',
        'vendor': 'Cisco',
        'start_u': 1,
        # 'end_u': 2
    }

    resp = requests.patch('http://127.0.0.1:8000/api/cmdb/devices/2/', json=data)
    print('status_code:', resp.status_code)
    print('resp_json:', resp.text)