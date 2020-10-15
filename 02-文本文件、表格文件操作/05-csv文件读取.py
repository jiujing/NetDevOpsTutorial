import csv

if __name__ == '__main__':
    '''
    逗号分隔值（Comma-Separated Values，CSV，有时也称为字符分隔值，因为分隔字符也可以不是逗号），
    其文件以纯文本形式存储表格数据（数字和文本）。
    纯文本意味着该文件是一个字符序列，不含必须像二进制数字那样被解读的数据。
    CSV文件由任意数目的记录组成，记录间以某种换行符分隔；每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符。
    通常，所有记录都有完全相同的字段序列。
    需要先open一个文件，将文件对象传入Python内置的csv对应的reader对象
    个人建议使用DictReader，写好表头，根据表头将数据转成dict的list
    '''
    with open('devs.csv', mode='r', encoding='utf8') as f:
        items = csv.DictReader(f)
        # 可以通过delimiter指定分隔符，常见的是逗号和制表符，默认是逗号
        # f_csv = csv.DictReader(f, delimiter='\t')
        for item in items:
            print(item)

    # 也可以使用reader，返回的rows ，每一个row是一行数据，一行数据格式是一个list，
    with open('devs.csv', encoding='utf8') as f:
        f_csv = csv.reader(f)
        # 读取第一行作为header，同时将文件指针指向下一行
        headers = next(f_csv)
        print('headers：', headers)
        for row in f_csv:
            print(row)
