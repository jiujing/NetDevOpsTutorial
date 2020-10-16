import re

if __name__ == '__main__':
    '''
    re.find 两个参数，第一个是正则的模式，第二个是待处理的字符串
    返回string中所有与pattern相匹配的match对象，返回形式为迭代器。
    '''

    line = '''   interface Ehternet1/5 is up
    interface Ehternet1/6 is up
    interface Ehternet1/7 is down
    '''
    intf_pattern = r'interface\s+Ehternet\d+/\d+'
    intf_match_list = re.finditer(intf_pattern, line)
    for intf in intf_match_list:
        print('intf find in  match::', intf.group(), '无子串默认返回的是字符串的list', type(intf))
