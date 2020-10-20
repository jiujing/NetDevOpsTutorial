from netmiko import ConnectHandler

if __name__ == "__main__":

    # dev_info = {
    #     'device_type': 'cisco_nxos',
    #     'ip': 'sbx-nxos-mgmt.cisco.com',
    #     'port': 8181,
    #     'username': 'admin',
    #     'password': 'Admin_1234!'
    # }
    #
    # with ConnectHandler(**dev_info) as dev_connection:
    #
    #     datas = dev_connection.send_command('show interface br', use_textfsm=True)
    #     for data in datas:
    #         print(data)


    '''
    没有对应模板的时候，返回的数据是show的原始内容
    '''
    # dev_info = {
    #     'device_type': 'huawei',
    #     'ip': '192.168.56.202',
    #     'port': 22,
    #     'username': 'netdevops',
    #     'password': 'Admin123!'
    # }
    #
    # with ConnectHandler(**dev_info) as dev_connection:
    #
    #     datas = dev_connection.send_command('display  interface bri', use_textfsm=True)
    #     print(datas)


