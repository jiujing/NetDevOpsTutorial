from netaddr import IPAddress, IPNetwork, IPGlob, IPRange, IPSet, iter_iprange, cidr_merge

if __name__ == '__main__':
    # ip set 去除重复的，得到一个最佳的set集合
    ips = [IPAddress('192.0.2.1'), '192.0.2.2/31', IPNetwork('192.0.2.4/31'), IPAddress('192.0.2.6'),
           IPAddress('192.0.2.7'), '192.0.2.8', '192.0.2.9', IPAddress('192.0.2.10'), IPAddress('192.0.2.11'),
           IPNetwork('192.0.2.12/30')]
    ip_set1 = IPSet(ips)
    print(ip_set1)

    '''set计算 合并网络或者地址 类似Python的计算 | 代表合并 ，并集计算'''
    new_ipset = IPSet(['192.0.2.0']) | IPSet(['192.0.2.1']) | IPSet(['192.0.2.2']) | IPSet(['192.0.2.3'])
    print(new_ipset)

    '''set计算 差集 类似Python的计算 - 从前者扣去后者，差集'''
    ipset1 = IPSet(['192.0.2.0']) | IPSet(['192.0.2.1']) | IPSet(['192.0.2.2']) | IPSet(['192.0.2.3']) |IPSet(['192.0.2.4'])
    ipset2= IPSet(['192.0.2.4'])
    print('ipset1-ipset2',ipset1-ipset2)

    '''set计算 对称差集 类似Python的计算 ^ 存在且只存在在一个IPSet里的网段'''
    ipset1 = IPSet(['192.0.2.0/24'])
    ipset2 = IPSet(['192.0.2.0/26'])
    print('ipset1^ipset2', ipset1 ^ ipset2)

    '''set计算 交集 类似Python的计算 & 在两个IPSet中共同存在的部分'''
    ipset1 = IPSet(['192.0.2.0/24'])
    ipset2 = IPSet(['192.0.2.0/26'])
    print('ipset1&ipset2', ipset1 & ipset2)