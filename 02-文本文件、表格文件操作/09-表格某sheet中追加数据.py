# --coding-- utf-8--
import pandas


def append_to_excel(filepath, dataframe) -> None:
    writer = pandas.ExcelWriter(filepath, mode='w')  # 这里的mode需要用w模式，a模式会产生新的sheet
    data = pandas.read_excel(writer, index_col=None, header=None)
    data.to_excel(writer, startrow=0, index=None, header=None, sheet_name='sheet1')
    dataframe.to_excel(writer, startrow=data.shape[0], index=None, header=None, sheet_name='Test01',engine="openpyxl")
    writer.save()


if __name__ == '__main__':
    df = pandas.DataFrame([['dedasd', '3', '223']], columns=None, index=None)
    # df.to_excel('追加.xlsx', sheet_name='Test01', index=False)
    # append_to_excel('追加.xlsx', df)
    append_to_excel('追加.xlsx', df)
