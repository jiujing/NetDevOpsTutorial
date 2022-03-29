from netmiko import ConnectHandler,Netmiko
from dev_info import nxosv9k

import logging

logging.basicConfig(
    level=logging.DEBUG,
)

if __name__ == '__main__':
    nxosv9k = {
    'device_type': 'cisco_ios',
    'host': '127.0.0.1',
    'username': 'admin',
    'password': 'admin',
    'port': 10008,  # optional, defaults to 22
    # 'secret': 'secret',  # optional, defaults to ''
}

    net_conn = Netmiko(**nxosv9k)
    # output = net_conn.send_command('display version')
    output = net_conn.send_command('show version')
    # 关闭连接
    net_conn.disconnect()
    print(output)