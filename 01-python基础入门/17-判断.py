if __name__ == '__main__':
    """
    if   必选，且排在一个判断流程的首位
    elif 可选，且一个判断流程可以多个elif
    else 可选，且排在判断流程的最后 
    """
    age = 19
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')

    # 结合字符串的一些运算，对于新手而言，可以解析很多网络配置信息。
    # 当然这不是解析网络配置的最优解，对于新手而言，是最快捷最易掌握的方法
    line = '''Eth1/1          1       eth  trunk  up      none                     1000(D) 11'''
    if line.startswith('Eth'):
        intf_name = line.split()[0]
        print('intf_name:', intf_name)
    else:
        print('此行，未发现端口信息')
