import re

if __name__ == '__main__':
    '''
    python中字符串有转义一说，所以写正则的时候建议大家在正则字符串的最前面写上r
    re.match 模块会从头匹配正则,两个参数，第一个是正则的模式，第二个是待处理的字符串
    从String首字母开始开始匹配pattern，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾
    match的时候pattern相当于隐式包含了一个^开始符在最前面
    '''
    line = 'interface Ehternet1/5 is up'
    intf_pattern = r'interface\s+Ehternet\d+/\d+'
    interface_match = re.match(intf_pattern, line)
    if interface_match:
        # 获取整体的匹配
        intf = interface_match.group()
        print('intf in group():', intf)

        # 同上，获取整体的匹配
        intf = interface_match.group(0)
        print('intf in group(0):', intf)
    # 以上这段代码，大家可以修改line 前面加一个空格，就会发现正则失效


    # 子串的提取 我们用"()"提取子串
    line = 'interface Ehternet1/5 is up'
    intf_pattern = r'interface\s+Ehternet(\d+)/(\d+)'
    interface_match = re.match(intf_pattern, line)
    if interface_match:
        # 获取整体的匹配
        intf = interface_match.group()
        print('intf in group():', intf)

        # 同上，获取整体的匹配
        intf = interface_match.group(0)
        print('intf in group(0):', intf)

        # 获取所有子串 groups()
        intf = interface_match.groups()
        print('intf in groups():', intf)

        # 获取指定index的子串 groups(index) 注意index不要越界
        intf = interface_match.group(1)
        print('intf index in groups(1):', intf)