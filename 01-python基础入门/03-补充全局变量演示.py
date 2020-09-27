g_a = 1
g_b = 2
g_c = 3


def func():
    # 局部变量声明并赋值，但是不会修改函数外的全局变量原始值
    g_a = 10
    g_b = 20
    # 声明全局变量引用，声明阶段不允许赋值
    global g_c
    # 全局变量赋值，这个时候全局变量已经由之前的3改变成为了现在的30
    g_c = 30
    print('局部变量:', g_a, g_b)
    print('global变量:', g_c)


if __name__ == '__main__':
    func()

    print('全局变量：', g_a, g_b, g_c)
