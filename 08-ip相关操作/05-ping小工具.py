from ping3 import ping, verbose_ping
import time
from datetime import datetime
import  logging


def ping_some_ip(host,src_addr=None):
    second = ping(host,src_addr=src_addr)
    return second

if __name__ == '__main__':
    host = 'www.baidu.com'
    src_addr = None
    # src_addr = '192.168.56.1'
    # 简单用法 ping地址即可，超时会返回None 否则返回耗时，单位默认是秒
    while True:
        print('kaishi ping @ {}'.format(datetime.now()))
        result = ping_some_ip(host,src_addr)
        if result is None:
            print('ping 失败！')
        else:
            print('ping-{}成功，耗时{}s'.format(host,result))
        time.sleep(5)