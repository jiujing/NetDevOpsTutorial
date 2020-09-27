if __name__ == '__main__':
    '''
    定义字符串用引号，1-3引号，但是需要一以贯之，前后一致
    个人推荐用单引号，小清新
    '''

    # 单引号定义
    my_1st_str = 'Hello World!'

    # 双引号定义
    my_2nd_str = "Hello World!"

    # 三引号定义
    my_3rd_str = """ this is my 3rd string.
Hello World！
    """

    print('1:', my_1st_str)
    print('2:', my_2nd_str)
    print('3:', my_3rd_str)

    # 字符串中有单引号，外侧建议使用双引号，反之亦然。
    a = 'py is short for "python" '
    print('a:', a)
    b = "py is short for 'python' "
    print('b:', b)
    # 避无可避的时候用\转义
    c = 'py is short for \'python\' '
    print('c:', c)
    d = "py is short for \"python\" "
    print('d:', d)

    # 多行字符串除了用三引号，也可以用括号加单（双）引号,区别是，三引号会保留换行，而这种方法会拼成一行。
    e = ('这是一个'
         '字符串'
         )
    print('e:', e)
