if __name__ == '__main__':
    """
    成员调整重点是append 追加，其他根据实际情况学习使用
    """
    # 追加一条数据
    devs = ['192.168.1.0', '192.168.1.2', '192.168.1.3']
    devs.append('192.168.1.4')
    print(devs)

    # 用insert在下标i 的位置插入一条数据
    devs.insert(1, '192.168.1.1')
    print('插入一条数据后：', devs)

    # 用pop函数删除一个元素，默认删除最后一个元素，也可以指定下标
    devs.pop()
    print('pop默认删除最后一条后：', devs)
    devs.pop(1)
    print('pop删除下标为1的数据后：', devs)

    # 两个列表合并
    # 用+合并 不改变原有的列表内容，会产生一个新列表（占内存）
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b
    print('合并列表ab：', c)

    # 用函数extend合并，在原有列表基础上追加另一个列表内容，内存损耗小
    a.extend(b)
    print('extend 合并两个列表：', a)
