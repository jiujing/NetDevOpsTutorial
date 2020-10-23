from netaddr import IPAddress, IPNetwork, IPGlob,IPRange,IPSet

if __name__ == '__main__':

    '''
    ## 网段相关操作
    # 定义网段 相当于有一个strict=False，也可以认为是ip_interface
    '''
    ip_net = IPNetwork('192.0.2.1/24')
    '''有几个重要的属性 '''
    '''ip位信息'''
    print(ip_net.ip)
    '''# 网络位信息'''
    print(ip_net.network)
    '''# 掩码信息，完整的掩码 形似255.255.255.0'''
    print(ip_net.netmask)
    '''# CIDR prefix bitmask,数字前缀的形式'''
    print('prefixlen is ', ip_net.prefixlen)
    '''# 实际严谨的网段信息'''
    print(ip_net.cidr)


    '''# 网络地址和广播地址'''
    net, broadcast = ip_net.network, ip_net.broadcast
    print('{}\'s net'.format(ip_net), net)
    print('{}\'s broadcast'.format(ip_net), broadcast)

    '''# 网络掩码和主机掩码'''
    netmask, hostmask = ip_net.netmask, ip_net.hostmask
    print('{}\'s netmask'.format(ip_net), netmask)
    print('{}\'s hostmask'.format(ip_net), hostmask)

    '''# 网段内的IP地址个数'''
    number_addr = ip_net.size
    print('{}\'s number_addr'.format(ip_net), number_addr)