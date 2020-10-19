from netmiko import ConnectHandler

if __name__ == "__main__":

    dev_info = {
        'device_type': 'cisco_nxos',
        'ip': 'sbx-nxos-mgmt.cisco.com',
        'port': 8181,
        'username': 'admin',
        'password': 'Admin_1234!'
    }

    with ConnectHandler(**dev_info) as dev_connection:

        datas = dev_connection.send_command('show interface br', use_textfsm=True)
        for data in datas:
            print(data)


