import sys

if __name__ == '__main__':
    '''
    python3 整数只有一种。区别python2还有长整数long。
    64位python3的整数范围是理论上是无限的，早期的Python2版本的范围是[-(max+1),max],max在python3中的表示如下代码演示
    不是做科学计算的话，我们可以不用于过分纠结这个问题，大家了解即可
    '''
    max_int = sys.maxsize
    print('整数最大值:', max_int)
    print('整数最小值:', -max_int - 1)

    # 默认十进制整数（0、正、负）
    a = 10
    b = -10
    c = 0
    print('默认10进制表示法：', a, b, c)

    # 2 8 16进制
    a = 0b11
    b = 0o12
    c = 0x1A
    print('打印时会做转换：', a, b, c)

    # 2 8 16通过内置函数构建,打印时会输出其书写格式
    a = bin(0b11)  # 可以使用进制书写的方法书写
    b = oct(10)  # 也可以使用十进制去书写
    c = hex(26)
    print('保留进制的书写格式：', a, b, c)
