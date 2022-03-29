import pandas as pd
def parse_show_int_bri(text):
    '''
    解析n9k的show int bri
    :param text: show的文本
    :return: 端口dict的list
    '''
    lines = text.splitlines()
    intfs = []
    for line in lines:
        line = line.strip()
        if line.startswith('Eth') and not line.startswith('Ethernet'):

            intf = line[0:16].strip()
            status = line[36:44].strip()
            reason = line[44:67].strip()
            intf_dict = {
                'intf':intf,
                'status':status,
                'reason':reason,
            }
            intfs.append(intf_dict)
    return intfs

def datas_to_excel(datas,file_name='datas.xlsx'):
    try:
        df = pd.DataFrame(datas)
        # sheetname大家按需填写，index是否显示索引 第几条数据（依然是从0开始数）
        df.to_excel(file_name, index=False)
        print('成功!')
    except Exception as e:
        print('异常，原因{}'.format(e))



def read_log(file,encoding='utf8'):
    with open(file,mode='r',encoding=encoding) as f:
        text = f.read()
        return text

if __name__ == '__main__':

    text = read_log(file='interfaces_bri.log')
    datas = parse_show_int_bri(text=text)
    datas_to_excel(datas)