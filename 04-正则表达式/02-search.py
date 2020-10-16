import re

if __name__ == '__main__':
    '''
    python中字符串有转义一说，所以写正则的时候建议大家在正则字符串的最前面写上r
    re.search 两个参数，第一个是正则的模式，第二个是待处理的字符串
    若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个。
    '''
    # 我们把line的开始加几个空格不影响我们在string中查找到我们想要的符合正则的子串
    line = '   interface Ehternet1/5 is up'
    intf_pattern = r'interface\s+Ehternet\d+/\d+'
    interface_match = re.search(intf_pattern, line)
    if interface_match:
        # 获取整体的匹配
        intf = interface_match.group()
        print('intf in group():', intf)

        # 同上，获取整体的匹配
        intf = interface_match.group(0)
        print('intf in group(0):', intf)



    # 子串的提取 我们用"()"提取子串
    line = 'interface Ehternet1/5 is up'
    intf_pattern = r'interface\s+Ehternet(\d+)/(\d+)'
    interface_match = re.search(intf_pattern, line)
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