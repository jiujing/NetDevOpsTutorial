if __name__ == '__main__':
    '''
    open 内置函数，打开一个文件，mode 默认是r，encoding 默认为空，会根据系统本身的编码方式进行编解码。我们的windows多是GBK
    强烈建议，大家在保存、打开文本文件的时候都统一使用utf8
    encoding 的utf8 大小写均可，也可以写成utf-8
    强烈建议，大家使用with+open打开文件，可以管理上下文，在程序离开的时候优雅的关闭文件，防止一些意外。
    '''
    f = open('test.txt', 'r', encoding='utf8')
    text = f.read()
    # 读取完内容后，建议关闭文件。
    f.close()
    print(text)

    # with open 上下文管理
    with open('test.txt', encoding='utf8') as f:
        text = f.read()
        print(text)
    # 退出with的管辖范围之后，文件被关闭，无法再次read访问打开。
    print(f.read())
