from netaddr import IPAddress, IPNetwork, IPGlob,IPRange,IPSet

if __name__ == '__main__':

    '''
    ## 网段相关操作
    # 定义网段 相当于有一个strict=False，
    使用中注意，实际相当于原生ipaddress中的ip_interface
    '''
    ip_net = IPNetwork('192.0.2.0/24')
    ip_net = IPNetwork('192.0.2.0/255.255.255.0')
    ip_net = IPNetwork('192.0.2.1/24')
    ip_net = IPNetwork('192.0.2/24')
    ip_net = IPNetwork('192.0.2.4/0.0.0.255')


