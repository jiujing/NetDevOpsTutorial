if __name__ == '__main__':
    # 定义一个字符串
    a = '''hosts: 192.168.1.1
   192.168.1.2
   192.168.1.3
   192.168.1.4 192.168.1.5
   ends'''

    # startswith，返回布尔型
    # 针对网络配置解析，多用于定位我们想要的数据的位置，所在行
    flag = a.startswith('hosts')
    print('a starts with hosts?:', flag)

    flag = a.startswith('ghost')
    print('a starts with ghost?:', flag)

    # endsswith 返回布尔型
    # 针对网络配置解析，多用于定位我们想要的数据的位置，所在行
    flag = a.endswith('ends')
    print('a ends with ends?:', flag)

    flag = a.endswith('end')
    print('a ends with ends?:', flag)

    # split，切片字符串成列表，默认用空白符,返回一个字符串的列表
    # 针对网络配置解析，我们在定位到行后，一般用空格机或者其他字符切割，加上一定判断，取出我们想要的数据（字符串）
    splited_strs = a.split()
    print('默认的切割效果，使用空白符，包括空格换行制表符等等：', splited_strs)
    # 使用指定的字符串去切割，只是演示，在本处没有任何意义，赋值的是sep这个参数，可以省略不写
    splited_strs = a.split('.')
    print('使用指定的字符串去切割：', splited_strs)

    # splitlines，讲文本以换行标志切割，返回的是字符串列表，每个字符串是文本的一行内容
    # 针对网络配置解析，将大段文本按行切割，针对每行去运行逻辑，结合split、startswith等其他函数加上判断，来提取有用信息
    # 初学者不用在意换行标志具体是什么
    lines = a.splitlines()
    print('splitlines,用换行标志切割字符串：', lines)

    # strip 去除左右的空白符，返回一个新的字符串，不改变原来的字符串结果
    # 有变种lstrip 和rstrip 只去除左侧或者右侧的空白符，空白符简单认定，没有实际形体的字符即可
    # 针对网络配置解析，很多字段左右会有空白符，为了使数据更准确，用此函数
    b = '\t 192.168.1.1    '
    print('strip去除左右的空白符--')
    # 打印后，多个空白符都被去除
    print(b.strip())

    # replace 将字符串中的子串用指定的字符串替换，返回一个新的字符串
    # 两个参数，第一个是old原有的字符串，第二个是要替换成的字符串
    # 使用场景非常多，比如端口缩写变为全拼，去除一些行内空格等等。
    b = a.replace('hosts', 'device ip list is：')
    print('a:', a)
    print('a after replaced:', b)

    # find 查找子串的起始位置，返回下标（计算机世界，下标从0开始），查找不到则返回-1.
    # 默认搜索区间是开始到最后，我们也可以指定区间，对应start和end两个参数
    # 针对网络配置解析，用于判断当前行是否有指定关键字，比如interface
    host_index = a.find('host')
    print('find host_index:', host_index)
    first_192_index = a.find('192')
    print('find first_192_index:', first_192_index)

    # index 基本等同find，唯一区别，查找不到子串，会抛出异常（报错）
    try:
        index_of_193 = a.index('193')
        print('index, 不可以找到子串情况下：', index_of_193)
    except Exception as e:
        print(e)

    # upper lower 将字符串转成全大写和全小写
    b = a.upper()
    c = a.lower()
    print('a upper is:', b)
    print('a lower is:', c)
