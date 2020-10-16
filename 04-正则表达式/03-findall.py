import re

if __name__ == '__main__':
    '''
    re.findall 两个参数，第一个是正则的模式，第二个是待处理的字符串
    返回string中所有与pattern相匹配的全部字串，返回形式为数组。
    无子串的时候list成员为字符串
    有子串的时候返回的list成员是符合要求的子串元组，不含整体
    比较适合两种情况
    一种是mac表的，类似的多行通过findll 匹配一次拿到所有数据
    一种是show interface，一段一段类似的内容，先通过正则+findall切分段，在每段里使用search或者match
    '''

    # 无子串
    line = '''   interface Ehternet1/5 is up
    interface Ehternet1/6 is up
    interface Ehternet1/7 is down
    '''
    intf_pattern = r'interface\s+Ehternet\d+/\d+'
    intf_match_list = re.findall(intf_pattern, line)
    for intf in intf_match_list:
        print('intf find::', intf, '无子串默认返回的是字符串的list', type(intf))

    # 有子串
    intf_pattern = r'interface\s+Ehternet(\d+)/(\d+)'
    intf_match_list = re.findall(intf_pattern, line)
    for intf in intf_match_list:
        print('intf slot and index info  find::', intf, '有子串默认返回的是子串的tuple', type(intf))
