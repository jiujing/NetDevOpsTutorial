from ncclient import manager
from device import huawei_ce_local as dev
# from device import nexus9k_info as dev

import logging

logging.basicConfig(
    level=logging.INFO,
)

if __name__ == '__main__':
    # dev = dict(username='admin',
    #                     password='Admin_1234!',
    #                     host='sbx-nxos-mgmt.cisco.com',# ip or hostname
    #                     hostkey_verify=False,# 关闭hostkey_verify是ssh验证
    #                     port=10000,# Netconf的协议端口，默认830，实验环境做了NAT
    #                     manager_params={'timeout': 180} # manager的一些参数，比如timeout
    #                     )
    # 上下文管理，用来连接设备。
    '''
    使用ncclient的manager包里的connect函数来创建一个netconf的连接，它会自动帮我们进行hello的创建
    常用参数下
                       username='netdevops',用户名
                       password='Admin123!', 密码
                       host='192.168.56.202', 设备IP
                       # 底层用到ssh ，因为我们用的是用户名密码认证，所以以下三个设置为False
                       hostkey_verify=False,
                       look_for_keys=False,
                       allow_agent=False,
                       # 默认端口是830
                       port=830,
                       # 一些参数的设置，一般是timeout，超时时间设置
                       manager_params={'timeout': 180},
                       # 设备的相关参数，一般用name为对应厂商进行优化。
                       device_params={'name': 'huawei'} # 加入此参数，可以优化
                       devices支持的厂商名称（取key的值）如下
                         supported_devices_cfg = {'junos':'Juniper',
                         'csr':'Cisco CSR1000v',
                         'nexus':'Cisco Nexus',
                         'iosxr':'Cisco IOS XR',
                         'iosxe':'Cisco IOS XE',
                         'huawei':'Huawei',
                         'huaweiyang':'Huawei',
                         'alu':'Alcatel Lucent',
                         'h3c':'H3C',
                         'hpcomware':'HP Comware',
                         'default':'Server or anything not in above'}
    '''
    with manager.connect(**dev) as m:
        '''调用字段属性server_capabilities和client_capabilities
           分别获取网络设备和我们程序支持的capabilities
        '''
        server_capabilities = m.server_capabilities
        client_capabilities = m.client_capabilities

        print('server_capabilities are:')
        for i in server_capabilities:
            print(i)
        print('client_capabilities are:')
        for i in client_capabilities:
            print(i)
        # # 根据设备的netconf软件层面实现的情况，部分不支持。
        # # 传入module的name，唯一标识
        # module_name  = 'openconfig-interfaces'
        # schema = m.get_schema(module_name)
        # with open("{}.yang".format(module_name), 'w') as f:
        #     # Write schema
        #     f.write(schema.data)