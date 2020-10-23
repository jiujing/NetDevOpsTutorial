from netaddr import IPAddress, IPNetwork, IPGlob,IPRange,IPSet

if __name__ == '__main__':
    '''
      定义IP地址,4 与6 是同一个类
    '''
    ip = IPAddress('192.0.2.1')
    print(ip, ip.version, type(ip))

    ip = IPAddress('2001:db8::1')
    print(ip, ip.version, type(ip))

    '''
       数字化转换
       转int 二进制 16进制
    '''
    ip = IPAddress('192.0.2.1')
    print('ip: {},整数格式:{}'.format(ip, int(ip)))
    print('ip: {},字符串格式:{}'.format(ip, str(ip)))
    print('ip: {},二进制格式:{}'.format(ip, bin(ip)))
    print('ip: {},16进制格式:{}'.format(ip, hex(ip)))
    # 二进制的带符号表示方式
    print('ip: {},进制的带符号表示方式:{}'.format(ip, ip.bits()))
    # 转成tuple 对应四个位置
    print('ip in 转成tuple 对应四个位置:',ip.words)


    '''
    ## 网段相关操作
    # 定义网段 相当于有一个strict=False，也可以认为是ip_interface
    '''
    ip_net = IPNetwork('192.0.2.0/24')
    ip_net = IPNetwork('192.0.2.0/255.255.255.0')
    ip_net = IPNetwork('192.0.2/24')
    ip_net = IPNetwork('192.0.2.4/0.0.0.255')

    print(ip_net)
    print(ip_net.ip)

    '''# CIDR prefix bitmask'''
    print('prefixlen is ',ip_net.prefixlen)

    '''# 网络地址和广播地址'''
    net, broadcast = ip_net.network, ip_net.broadcast
    print('{}\'s net'.format(ip_net),net)
    print('{}\'s broadcast'.format(ip_net),broadcast)

    '''# 网络掩码和主机掩码'''
    netmask, hostmask = ip_net.netmask, ip_net.hostmask
    print('{}\'s netmask'.format(ip_net), netmask)
    print('{}\'s hostmask'.format(ip_net), hostmask)

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


    '''# 网段规划 subnet,是一个迭代对象，可以用list强制转换'''
    ip_net = IPNetwork('172.24.0.0/24')
    subnets = ip_net.subnet(26)
    print(subnets,type(subnets))
    print(list(subnets))

    '''# 不支持overlaps 可以用in 判断网段是否有重叠（或者说是归属关系）'''
    ip_net1 = IPNetwork('172.24.0.0/24')
    ip_net2 = IPNetwork('172.24.0.0/25')
    overlaps = ip_net1 in ip_net2 or ip_net2 in ip_net1 # 计算优先级拿不准的可以用圆括号把or 前后分别用()括号圈起来
    print(overlaps)

    # 强大的人性化的IP段的书写方式支持 IPGlob
    '''
     IP glob          | Description                  |
    +==================+==============================+
    | ``192.0.2.1``    | a single address             |
    +------------------+------------------------------+
    | ``192.0.2.0-31`` | 32 addresses                 |
    +------------------+------------------------------+
    | ``192.0.2.*``    | 256 addresses                |
    +------------------+------------------------------+
    | ``192.0.2-3.*``  | 512 addresses                |
    +------------------+------------------------------+
    | ``192.0-1.*.*``  | 131,072 addresses            |
    +------------------+------------------------------+
    | ``*.*.*.*``      | the whole IPv4 address space |
    '''
    ip_list = IPGlob('192.0.2.*')
    ip_list = IPGlob('192.0.2.1-19')
    ip_net = IPNetwork('192.0.2.0/24')
    print(ip_list in ip_net)

    print(list(ip_list))


    # 起始
    ip_list = IPRange('192.0.2.1', '192.0.2.21')
    print(ip_list)
    # 肯恩的cidr地址段
    ip_net = ip_list.cidrs()
    print(ip_net)

    # ip set 去除重复的，得到一个最佳的set集合
    ips = [IPAddress('192.0.2.1'), '192.0.2.2/31', IPNetwork('192.0.2.4/31'), IPAddress('192.0.2.6'),
           IPAddress('192.0.2.7'), '192.0.2.8', '192.0.2.9', IPAddress('192.0.2.10'), IPAddress('192.0.2.11'),
           IPNetwork('192.0.2.12/30')]
    ip_set1= IPSet(ips)
    print(ip_set1)