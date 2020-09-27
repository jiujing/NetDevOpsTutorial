if __name__ == '__main__':
    '''
    切片
    简单理解就是取list（tuple、str等，可以通过index访问）的一小部分
    x_list[start:end:step],start代表的是从哪里开始，end是代表在哪里结束，左开有笔取的是list的[start,end)之间的数据，没取到end
    可以设置步长，step默认1
    start，end不写，分别代表两端，也可以是负值，只要不越界，不矛盾即可
    '''
    a = [0, 1, 2, 3, 4, 5, 6]
    # 取index[1,4)之间的值，不包含a[4]
    print('a[1:4]:', a[1:4])
    # index从2取到最后
    print('a[2:]:', a[2:])
    # 可以取负值
    print('a[-3:]:', a[-3:])

    # 设置步长
    print('a[::3]', a[::3])
    print('a[0:5:2]', a[0:6:2])
    # 巧用切片，逆转list
    print('a[::-1]', a[::-1])

    '''
    dict 的迭代，
    for循环dict对象，可以用key值进行迭代
    '''
    dict_obj = {
        '192.168.1.1': 'sw01',
        '192.168.1.2': 'sw02',
        '192.168.1.3': 'sw03'
    }
    for k in dict_obj:
    #等同 for k in dict_obj.keys()：
        print('k:', k)
        print('v:', dict_obj[k])
    dict_obj = {
        '192.168.1.1': 'sw01',
        '192.168.1.2': 'sw02',
        '192.168.1.3': 'sw03'
    }
    for k, v in dict_obj.items():
        print('k:', k)
        print('v:', v)
