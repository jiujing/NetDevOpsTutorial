import ipaddress

if __name__ == '__main__':
    '''
    ipaddress 是Python内置的一个IP模块，日常的IP相关操作基本都可以处理。
    构建一个ip地址对象，使用ip_address 会根据地址类型自动判断v4 v6
    '''
    # v4
    ip = ipaddress.ip_address('192.0.2.1')
    print('ip:', ip, ',type:', type(ip))

    # v6
    ip = ipaddress.ip_address('2001:db8::1')
    print('ip:', ip, ',type:', type(ip))

    # 也可以显示指定用哪个版本的IP地址
    ip = ipaddress.IPv4Address('192.0.2.1')
    print('ip:', ip, ',type:', type(ip))

    ip = ipaddress.IPv6Address('2001:db8::1')
    print('ip:', ip, ',type:', type(ip))

    # 定义网络，同样也可以显示定义IPv4的网段或者v6的网段
    net = ipaddress.ip_network('192.0.2.0/24')
    print('network:', net, ',type:', type(net))

    net = ipaddress.ip_network('2001:db8::0/96')
    print('network:', net, ',type:', type(net))

    net = ipaddress.IPv4Network('192.0.2.0/24')
    print('network:', net, ',type:', type(net))

    net = ipaddress.IPv6Network('2001:db8::0/96')
    print('network:', net, ',type:', type(net))

    '''
    网络对象不能设置任何主机位。 
    比如用192.0.2.1/24定义网络段是不严谨的，会报错，如果要放宽限制，需要把参数strict=False，
    程序会自动调整为规范的网络段
    大家可以把下面的代码strict去掉试试
    '''
    net = ipaddress.ip_network('192.0.2.1/24', strict=False)
    print('network:', net, ',type:', type(net))

    '''
    定义接口的时候，我们会有接口的地址与所属段信息，这个时候我们可以使用interface
    '''
    ip_intf = ipaddress.ip_interface('192.0.2.13/29')
    print('ip_interface:', ip_intf, ',type:', type(ip_intf))
    # 保留主机地址的时候同时保留了网段信息,注意，调用是属性，不是方法
    ip_intf_net = ip_intf.network
    print('ip_intf_net:', ip_intf_net, ',type:', type(ip_intf_net))
    #查看网段中有多少地址
    num_addresses = ip_intf_net.num_addresses
    print('{}中有{}个地址'.format(ip_intf_net,num_addresses))
    # 取出所有的主机地址（去0和255） 网段对象后用hosts()方法，但是返回的是一个迭代对象，打印出来并不是所有的IP地址
    print('all hosts generator:',ip_intf_net.hosts())

    net = ipaddress.ip_network('192.0.2.0/24', strict=False)
    # 打印出所有主机位地址
    for i in net.hosts():
        print(i)

    # 打印出所有地址 含0 255 与上面的区别开，大家可以把
    for i in net:
        print(i)

    # 判断一个地址是否属于某网段
    ip = ipaddress.ip_address('192.168.1.23')
    net = ipaddress.ip_network('192.168.1.0/24')
    print('{} in {}?:'.format(ip,net),ip in net)

    # 可以通过下标取地址
    print(net[100])

    # 划分子网,传入新的子网掩码
    net = ipaddress.ip_network('192.168.1.0/24')
    subnets = net.subnets(new_prefix=28)
    print('掩码的方式划分子网')
    for i in subnets:
        print(i)
    # 划分子网，子网掩码差异的方式，比如输入5 则当前子网掩码24+5 新子网掩码是29
    net = ipaddress.ip_network('192.168.1.0/24')
    subnets = net.subnets(prefixlen_diff=5)
    print('子网个数的方式划分子网')
    for i in subnets:
        print(i)


    # 寻找包含此网段的更大的网段
    supernet = net.supernet(new_prefix=17)
    print(supernet)

    # 两个网段是否有包含关系,正反均可
    net1 = ipaddress.ip_network('192.168.1.0/24')
    net2 = ipaddress.ip_network('192.168.1.0/25')
    print(net1.overlaps(net2))
    print(net2.overlaps(net1))

    # 地址的多形式输出
    ip = ipaddress.ip_address('192.168.1.23')
    print('{} 字符串：'.format(ip),str(ip))
    print('{} 整数：'.format(ip),int(ip))
    # 不支持转二进制，需要转int后再转二进制bin
    print('{} 二进制：'.format(ip),bin(int(ip)))
