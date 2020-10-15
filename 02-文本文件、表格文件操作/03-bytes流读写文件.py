if __name__ == '__main__':
    '''
       针对一些字节流的二进制文件，比如通过web获取的图片，或者是其他字节流，我们希望把它写入文件中
       也是使用open创建文件 ，mode='wb'，代表的是写入文件,无需指定编码格式，相当于一个搬运工
    '''
    # with open 上下文管理 打开一个二进制文件 图片 用rb读取，代表去读字节流
    with open('test_bytes.png', mode='rb') as f:
        content = f.read()
        print('png bytes content is:', content)
        # 以上等同于
        # 注意 writelines 不会写入换行，需要我们自己加。
    with open('test_bytes_dest.png', mode='wb') as dest_f:
        dest_f.write(content)
