if __name__ == '__main__':
    """
    列表是一个序列，类似数组，序列里的元素可以是同一类型，也可以是异构类型
    通过下标访问成员，下面从0开始到{列表长度-1}，越界访问会报错
    """
    # 整齐划一的数据
    devs = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
    # 异构数据
    dev_info = ['192.168.1.1', 'dev01', 22]

    # 访问成员
    dev_ip = dev_info[0]
    dev_name = dev_info[1]
    ssh_port = dev_info[2]
    print('dev_ip:', dev_ip)
    print('dev_name:', dev_name)
    print('ssh_port:', ssh_port)

    # 访问成员 可以从后往前数，-1代表最后一个，以此类推
    ssh_port = dev_info[-1]
    print('ssh_prot(accessed by "-1" index):', ssh_port)

    # 列表长度计算，使用len() 内置函数
    dev_info_len = len(dev_info)
    print('dev_info_len:', dev_info_len)

    # 越界访问会报错,能访问的范围是0到{列表长度-1}
    print(dev_info[len(dev_info)])

    # 补充 空列表
    a = []
    print('空列表：', a)
