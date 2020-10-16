import re

if __name__ == '__main__':
    '''
    之前的方法每次执行match search等的时候，会先编译正则 再解析 每次执行都会消耗资源
    对于循环使用的，我们可以先编译再调用对应的match、search方法，减少资源消耗
    '''
    lines = '''   interface Ehternet1/5 is up
        interface Ehternet1/6 is up
        interface Ehternet1/7 is down
        '''
    intf_re = re.compile(r'interface\s+Ehternet(\d+)/(\d+)')

    for line in lines.splitlines():
        interface_match = intf_re.search(line)
        if interface_match:
            print(interface_match.group())
    '''
       对于比较复杂的正则，我们可以一段段写起，慢慢添加，形成复杂的正则
       过于复杂的正则，建议拆解开分而治之
    '''

    '''
    split可以按正则切割字符串
    '''
    line = '''interface Ehternet1/5 is up
        interface Ehternet1/6 is up
        interface Ehternet1/7 is down
        '''
    intf_pattern = r'interface\s'
    items = re.split(intf_pattern, line)
    print(items)

    '''
       sub相当于replace，三个参数 正则，符合正则的字符串要被替换的内容，执行的字符串
    '''
    intf_pattern = r'interface'
    line_after_sub = re.sub(intf_pattern, 'Interface', line)
    print(line_after_sub)
