if __name__ == '__main__':
    '''
    文件过大，一次性读入会使内存消耗，甚至溢出
    比较pythonic的方法是如下
    它会一行一行的打开文件，不会像read那样一次性读出所有的，我们根据实际文件大小去定，如果性能出现问题，可以如此调整
    '''
    with open('test.txt', mode='r', encoding='utf8') as file:
        for line in file:
            print(line)
    '''
    # 还有以下方法供参考，逐行读文件，不会一次加载
    # '''
    with open('test.txt', 'r', encoding='utf8') as file:
        while True:
            # readline会读一行然后将，file指针指向下一行。
            line = file.readline()
            print('while+readline:', line)
            if not line:
                break
