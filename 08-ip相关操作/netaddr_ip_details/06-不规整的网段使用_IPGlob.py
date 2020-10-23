from netaddr import IPAddress, IPNetwork, IPGlob,IPRange,IPSet,iter_iprange, cidr_merge

if __name__ == '__main__':
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
    ip_list = IPGlob('192.0.2.0-15')
    ip_net = IPNetwork('192.0.2.0/24')
    # 可以判断网段归属
    print(ip_list in ip_net)

    # 把一堆IP或者可迭代的IP网段合并到尽可能小的一组cidr网段中去，适用于所有的IP地址和IP网段对象
    # 通过演示去感受一下
    ip_list = IPGlob('192.0.2.0-15')
    ip_list = IPGlob('192.0.2.0-16')
    ip_list = IPGlob('192.0.2.0-19')
    ip_list = IPGlob('192.0.2.0-20')
    # 调用函数cidr_merge
    ip_net_new= cidr_merge(ip_list)
    print(ip_net_new)
    # 等同于在一个IP（网段）对象中调用cidrs这个函数
    ip_net_new_with_cidr = ip_list.cidrs()
    print(ip_net_new_with_cidr)