nexus9k_info = dict(username='admin',
                    password='Admin_1234!',
                    # connect()方法，连接工具，返回一个连接对象
                    # 默认netconf服务器端是830端口,hostkey_verify是ssh验证问题
                    host='sbx-nxos-mgmt.cisco.com',
                    device_params={'name': 'nexus'},
                    hostkey_verify=False,
                    port=10000,
                    manager_params={'timeout': 180}
                    )

huawei_ce_local = dict(username='netdevops',
                       password='Admin123!',
                       # connect()方法，连接工具，返回一个连接对象
                       # 默认netconf服务器端是830端口,hostkey_verify是ssh验证问题
                       host='192.168.56.202',
                       # device_params={'name': 'nexus'},
                       hostkey_verify=False,
                       look_for_keys=False,
                       allow_agent=False,
                       port=830,
                       manager_params={'timeout': 180},
                       device_params={'name': 'huawei'} # 加入此参数，可以优化
                       )
