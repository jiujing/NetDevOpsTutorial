from netaddr import IPAddress, IPNetwork, IPGlob, IPRange, IPSet

if __name__ == '__main__':

    ip_net = IPNetwork('192.168.1.0/24')
    '''# 网段内的IP地址个数'''
    number_addr = ip_net.size
    print('{}\'s number_addr'.format(ip_net), number_addr)

    '''# 迭代一个网段内的地址'''
    ip_net = IPNetwork('192.0.2.0/30')
    for ip in ip_net:
        print(ip, type(ip))

    '''# 网段长度 支持len 网段还支持list转换，这个是优于原生的'''
    print('{} len is'.format(ip_net), len(ip_net))
    print('{} list is'.format(ip_net), list(ip_net))

    '''# 网段支持索引和切片，优于原生，原生无切片'''
    print(ip_net[0])
    print(ip_net[-1])
    '''#切片返回的是一个可迭代对象'''
    print(ip_net[0:2])
