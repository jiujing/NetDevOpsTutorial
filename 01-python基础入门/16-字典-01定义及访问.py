if __name__ == '__main__':
    """
    dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
    无法通过下标访问
    花括号定义或者dict(k1=v1,k2=v2)的形式定义
    """
    # {}定义,key值在初学阶段简单理解成字符串即可（实际是可以被hash的对象均可），key值不可重复
    # 也可以用int去做key值，本人很少使用，可读性比如str作为key值
    dev_info = {
        'dev_name': 'sw01',
        'ip': '192.168.1.1',
        'ssh_port': 22
    }
    print('dict:', dev_info)

    # 通过dict方式构建
    dev_info = dict(dev_name='sw01', ip='192.168.1.1', ssh_port=22)
    print('dict:', dev_info)

    # 访问成员
    # 方括号加key值访问对应value，key不存在报错
    # get方法获取对应key的value，key不存在会返回指定值，如无指定返回None

    # 方括号访问
    ip = dev_info['ip']
    print('ip:', ip)

    # get方法访问
    ip = dev_info.get('ip')
    print('ip:', ip)

    username = dev_info.get('username', 'admin')
    print('username:', username)
