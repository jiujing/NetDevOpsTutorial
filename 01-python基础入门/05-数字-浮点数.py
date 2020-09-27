from decimal import Decimal

if __name__ == '__main__':
    # 浮点数普通表示法
    a = 3.2
    b = 4.11
    print('浮点数普通表示法:', a, b)

    # 科学计数法
    a = 1.23e2  # 等同于1.23*10^2
    b = 1.23e-18  # 等同于1.23*10^-18
    print('浮点数科学表示法:', a, b)

    # 浮点数的计算是不精确的，对于精确度比较敏感的场景，请使用Decimal 会有性能损耗。

    a = 3.2
    b = 4.11
    print('不精准的浮点数计算:b-a=', b-a)

    a = Decimal('2.1')
    b = Decimal('4.2')
    c = a + b
    print(c)
    print(c == Decimal('6.3'))