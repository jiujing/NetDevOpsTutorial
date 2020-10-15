import pandas as pd

if __name__ == '__main__':
    raw_data = [{'name': 'John', 'age': 30, 'gender': 'male'}, {'name': 'Mary', 'age': 22, 'gender': 'female'},
                {'name': 'Smith', 'age': 32, 'gender': 'male'}]
    df = pd.DataFrame(raw_data)
    # sheetname大家按需填写，index是否显示索引 第几条数据（依然是从0开始数）
    df.to_excel('pandas_output.xlsx', sheet_name='Test01',index=False)
    # df.to_csv('pandas_output.csv', index=False)