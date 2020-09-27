if __name__ == '__main__':
    # 变量无需指定变量的类型（python的福利），无需事先定义，可随时定义并赋值。
    # 变量先定义赋值后才可以使用
    # 赋值使用一个等号“=”，赋值符号的左右建议各一个空格，方便阅读：）
    a = 1
    b = 2
    c = 3
    print(a, b, c)

    # 可使用以下语法糖对多个相同值赋值
    a = b = c = 10
    print(a, b, c)

    # 也可以使用以下语法糖对于一系列变量一次完成赋值
    a, b, c = 1, 2, 3
    print(a, b, c)

    # 普通变量建议使用蛇形命名法
    device_name = 'AS001'
    device_start_u = 10
    print(device_name, device_start_u)

    # 对于全局变量

