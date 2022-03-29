from netmiko import Netmiko


if __name__ == '__main__':
    dev_info = {
        'ip':'127.0.0.1',
        'port':10000,
        'username':'admin',
        'password':'admin',
        'device_type':'cisco_xr'
    }
    conn = Netmiko(**dev_info)
    output = conn.send_command('show version')
    print(output)