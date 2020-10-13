import csv

if __name__ == '__main__':
    '''
    对于初学者，我们也推荐DictWriter读取数据，可以通过dict的list写入数据
    在写入数据之前先用open打开一个可以写的文件，重点是在new_line='',不然打开的时候会多一个空行。
    然后调用wirter构建一个csv的写入对象，DictWriter构建时一定要传入filednames,表头。
    默认的writer的无需写header
    
    '''
    ## 读取到字典去中
    with open('devs4write1.csv', 'w', encoding='utf8', newline='') as f:
        headers = ['ip', 'area', 'role']
        rows = [{
            'ip': '192.168.1.1',
            'area': 'a',
            'role': 'as'
        },
            {
                'ip': '192.168.1.2',
                'area': 'a',
                'role': 'as'
            },

            {
                'ip': '192.168.1.3',
                'area': 'a',
                'role': 'as'
            },
        ]
        # 构建写入csv的对象
        csv_writer = csv.DictWriter(f, headers)
        # 写写表头，再写数据，如果不写表头，则最后的数据没有表头。
        csv_writer.writeheader()
        csv_writer.writerows(rows)

    # 一般比较通用的办法是，是写数组，每组是一行数据。
    with open('devs4write2.csv', 'w', encoding='utf8', newline='') as f:
        headers = ['ip', 'area', 'role']
        rows = [['192.168.1.1', 'A', 'AS'],
                ['192.168.1.2', 'A', 'AS'],
                ['192.168.1.3', 'A', 'AS'],
                ['192.168.1.4', 'A', 'AS']]
        csv_writer = csv.writer(f)
        # writerow写入一行数据
        csv_writer.writerow(headers)
        # writerows 写入多行数据，传入列表的列表。
        csv_writer.writerows(rows)
