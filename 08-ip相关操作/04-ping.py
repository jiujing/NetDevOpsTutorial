from ping3 import ping, verbose_ping

if __name__ == '__main__':
    # 简单用法 ping地址即可，超时会返回None 否则返回耗时，单位默认是秒
    second = ping('www.baidu.com')
    print('it took {} second'.format(second))

    '''
        返回的是ping包响应的秒数，如ping不同，则为None
        dest_addr: 可以是域名和IP 例"192.168.1.1"/"example.com"
        timeout: 默认超时时间是4 单位秒。同windows
        unit: 返回的耗时时间单位，，"s" for seconds, "ms" for milliseconds. 默认是"s"
        src_addr: WINDOWS ONLY. 从哪个网络ping出 Ex. "192.168.1.20". (default None)
        interface: LINUX ONLY. 从哪个网络ping出. Ex. "wlan0". (default None)
        ttl:默认为None, 64 onLinux and macOS, and 128 on Windows. (default None)
        seq: ICMP packet sequence, usually increases from 0 in the same process. (default 0)
        size: 默认56, same as in macOS. (default 56) 小于MTU1480

    '''
    '''
       verbose_ping 类似我们在窗口ping
       count: ping的次数，默认是4
       interval: ping的间隔，默认是0，0代表上一个结束，下一个立即开始 
    
    '''
    verbose_ping('www.baidu.com',count=4,interval=0)