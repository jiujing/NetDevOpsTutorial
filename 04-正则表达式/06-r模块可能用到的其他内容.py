import re

if __name__ == '__main__':
    '''
    split(intf_pattern, line)
    用正则切割字符串，返回字符串列表
    '''

    line = '''   interface Ehternet1/5 is up
    interface Ehternet1/6 is up
    interface Ehternet1/7 is down
    '''
    intf_pattern = r'interface\s+Ehternet\d+/\d+'
    split_strs = re.split(intf_pattern, line)
    for split_str in split_strs:
        print(split_str)

    '''
        sub(pattern,new_str, whole_str)
        用new_str替换字符串中所有符合条件的内容
    '''

    line = '''   interface Ehternet1/5 is up
        interface Ehternet1/6 is up
        interface Ehternet1/7 is down
        '''
    intf_pattern = r'Ehternet\d+/\d+'
    str_after_replace = re.sub(intf_pattern, '{interfacename}', line)
    print(str_after_replace)
