from netaddr import IPAddress, IPNetwork, IPGlob,IPRange,IPSet,iter_iprange, cidr_merge

if __name__ == '__main__':
    '''IPRange如其名，指定起止IP地址，实现'''
    ip_list = IPRange('192.0.2.1', '192.0.2.21')
    # print(ip_list)
    # # 最适合的cidr地址段
    # ip_net = ip_list.cidrs()
    # print(ip_net)
    for i in ip_list:
        print(i)