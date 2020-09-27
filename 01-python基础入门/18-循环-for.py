if __name__ == '__main__':
    """
    for循环，依次将list tuple set中的元素迭代
    实际for循环可以针对所有的可迭代对象进行迭代循环，初学阶段，可以简单理解以上几种可以迭代的数据类型
    语法大体如下
    for iterating_var in sequence:
        statements(s)
    """
    a = [1, 2, 3, 4, 5]
    # a = (1, 2, 3, 4, 5)
    # a = {1, 2, 3, 4, 5}
    # a = '12345'
    for i in a:
        print(i, end=' ')

    print('\n')
    # 通过索引访问
    # 需要借助range这个内置的函数
    # range(start,stop,step) 三个参数，start 默认0 ，step是步长，默认1
    for i in range(len(a)):
        print('index:', i, end=' ')
        print('value:', a[i], end=',')

    print('\n')
    for i in a:
        # 等于2的时候,continue以下的逻辑块不会执行，所以不会打印2
        if i == 2:
            continue
        print(i, end=' ')

    print('\n')
    for i in a:
        # 等于2的时候不会打印数字，break会直接终止循环，所以不会打印2及以后的所有数字
        if i == 2:
            break
        print(i, end=' ')
