import pandas as pd
import netmiko
if __name__ == '__main__':
    '''
    pandas是一个科学计算的包，但是我们可以借助于它对表格数据的读写
    在使用前使用pip install pandas xlwt xlrd
    read_excel读取表格pd.read_excel('example.xlsx', sheet_name='Sheet1')
    read_csv读取csv pd.read_excel('example.csv')
    读取的是pd的专属的dataframe格式，转为字典list需要调用to_dict(orient='records')
    '''
    dataframe = pd.read_csv('devs.csv')
    items = dataframe.to_dict(orient='records')
    print(items)

    '''
    写入文件基本也一样
    先用字典list构建dataframe
    然后逆向，dataframe写入文件 用to_excel
    '''
    raw_data = [{'name': 'John', 'age': 30, 'gender': 'male'}, {'name': 'Mary', 'age': 22, 'gender': 'female'},
                {'name': 'Smith', 'age': 32, 'gender': 'male'}]
    df = pd.DataFrame(raw_data)
    # sheetname大家按需填写，index是否显示索引 第几条数据（依然是从0开始数）
    df.to_excel('pandas_output.xlsx', sheet_name='Test01', index=True)
    df.to_csv('pandas_output.csv', index=False)
