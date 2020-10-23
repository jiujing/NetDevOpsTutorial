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