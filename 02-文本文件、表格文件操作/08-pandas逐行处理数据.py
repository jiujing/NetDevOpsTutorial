import pandas as pd

'''
提供一种思路，pandas 可以逐行梳理数据
1、构建一个pandas的二维数据结构，DataFrame（用字典或者从文件读取均可）
2、写一个函数func dataframe调用apply函数，apply函数有两个参数
   第一个是每行要应用（apply）的函数，我们赋值为我们定义的func
   另外一个是axis=1代表我们按行去处理
3、把每行函数处理返回的新赋值给dataframe对象的一个新的key
4、用dataframe写入数据到表格文件。

'''
def gen_desc(row):
    # print(row) # 可以打印一下看看row 它是每一行的一个字典，如{'name': 'eth1/1', 'to_server': 'XX_DB'} 非常易用
    desc_config_templ = '''
interface {interface}
    description connected to {to_server}
    '''
    desc_config = desc_config_templ.format(interface=row['name'], to_server=row['to_server'])
    return desc_config


if __name__ == '__main__':
    raw_data = [
        {'name': 'eth1/1', 'to_server': 'XX_DB'},
        {'name': 'eth1/2', 'to_server': 'XX_app'},

    ]
    df = pd.DataFrame(raw_data)
    print(df)
    df['desc_config'] = df.apply(gen_desc, axis=1)
    df.to_excel('desc_config.xlsx',sheet_name='interface_config',index=False)
