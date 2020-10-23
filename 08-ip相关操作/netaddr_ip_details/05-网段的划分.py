from netaddr import IPAddress, IPNetwork, IPGlob, IPRange, IPSet

if __name__ == '__main__':
    '''划分子网 subnet,是一个迭代对象，for循环访问，也可以用list强制转换后访问
       根据网段大小判断使用哪种方法，大的话，一定要用for访问'''
    ip_net = IPNetwork('172.24.0.0/24')
    subnets = ip_net.subnet(26)
    # # count可以约束返回的子网数量
    # subnets = ip_net.subnet(30,count=10)
    print(subnets, type(subnets))
    print(list(subnets))

    '''
        计算超网Supernets 函数 supernet(prefixlen)
        一路返回可能的超网，自顶而上  
    '''
    ip_net = IPNetwork('172.24.0.0/24')
    prefixlen = 22
    supernets = ip_net.supernet(prefixlen)
    for i in supernets:
        print('{}超网，prefix{}'.format(ip_net, prefixlen), i)

    '''#判断网段是否有重叠归属关系 不支持overlaps 可以用in 判断网段是否有重叠（或者说是归属关系）'''
    ip_net1 = IPNetwork('172.24.0.0/24')
    ip_net2 = IPNetwork('172.24.0.0/25')
    overlaps = (ip_net1 in ip_net2) or (ip_net2 in ip_net1)  # 计算优先级拿不准的可以用圆括号把or 前后分别用()括号圈起来
    print(overlaps)
