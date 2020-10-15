if __name__ == '__main__':
    '''
    open 内置函数，打开一个文件，mode 使用w 表示写入内容.每次会清空原有的内容。如果是追加，mode=a
    encoding 读写的时候都统一使用utf8
    强烈建议，大家使用with+open打开文件，可以管理上下文，在程序离开的时候优雅的关闭文件，防止一些意外，尤其是写文件的时候。
    通过打开对象的write方法写入字符串 也可以用writelines写入一个列表
    '''


    # with open 上下文管理
    with open('test_w.txt', mode='w', encoding='utf8') as f:
        lines = [
            'this is my text for write,',
            'hello world!',
            'bye'
        ]
        # 注意 writelines 不会写入换行，需要我们自己加。
        f.writelines(lines)
        # 以上等同于以下
        lines = [
            'this is my text for write,\n',
            'hello world!\n',
            'bye\n'
        ]
        # 注意 writelines 不会写入换行，需要我们自己加。
        for line in lines:
            f.write(line)
