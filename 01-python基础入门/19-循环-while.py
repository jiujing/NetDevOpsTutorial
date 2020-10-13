if __name__ == '__main__':
    '''
    while {condition}:
        {code_block}
    while循环一般分两种：
    一种是通过计数器控制循环
    一种是while True,一直循环，在循环内部进行一些判断，比如时间或者找到自己想要的结果通过break跳出循环
    二者也可以结合起来
    '''
    n = 1
    while n < 20:
        print('n:', n, end=',')
        n += 1
    print('循环结束')

    while True:
        num = input('请输入一个数字')
        if num == '100':
            print('恭喜你猜对了')
            break
