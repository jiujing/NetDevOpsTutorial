from IPy import IP,IPSet

if __name__ == '__main__':
    '''
    Class for handling IP addresses and networks
    可以创建IP地址和网络 是一个复合类
    '''
    ip = IP('192.168.2.1')
    ip_net = IP('192.168.2.0/24')
    print(ip, type(ip))
    print(ip_net, type(ip_net))

    for i in ip_net:
        print(i, type(i))

    # 网段 掩码及prefix
    ip_net = IP('127.0.0.0/24')
    ip_net = IP('127.0.0.0/255.255.255.0')
    # 范围表示，但是必须是一个完整的网段
    ip_net = IP('127.0.0.0-127.0.0.255')
    print(ip_net)

    #
    # ip_interface 或者是strict = False

    ip_net = IP('127.0.0.1/255.0.0.0', make_net=True)
    # 以上等同于以下
    ip_net = IP('127.0.0.1').make_net('255.0.0.0')

    print(ip_net, ip_net.net(), ip_net.netmask())

    # 两个IP相关对象是否有交集
    ip_net1 = IP('172.24.0.1')
    ip_net2 = IP('172.24.0.0/25')
    ip_net3 = IP('192.24.0.0/25')
    # 0代表无重叠，1代表前者包含后者，-1代表前者被后者包含
    print(ip_net1.overlaps(ip_net2))
    print(ip_net2.overlaps(ip_net1))
    print(ip_net3.overlaps(ip_net1))
    print(ip_net1.overlaps(ip_net3))


    # IPSet 多网段 类似集合的运算，会根据情况自动的拆分合并成最适合的网段

    ip_net_set = IP('10.0.0.0/22') - IP('10.0.2.0/24')
    print(ip_net_set)

    ip_net_set = IPSet([IP('10.0.0.0/23'), IP('10.0.3.0/24'), IP('10.0.2.0/24')])
    print(ip_net_set)

    # IPy 简单情况下可使用，数据结构不够细致，IP与network混用，但是IPSet对象又独树一帜，在一些情况下用户比较大。比如合并网段。

