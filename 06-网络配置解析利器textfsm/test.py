from textfsm import TextFSM

if __name__ == '__main__':
    '''
    从textfsm导入TextFSM类，实例化的时候传入的是一个IO文件对象，不是字符串，这点一定要注意。
    实例化后，调用函数ParseTextToDicts，传入参数我们show出来的网络配置，即可解析出来字典的列表。
    '''
    with open('case01.log', 'r', encoding='utf8') as f:
        dev_text = f.read()
    template = TextFSM(open('case01.textfsm', encoding='utf8'))
    infos = template.ParseTextToDicts(dev_text)
    for i in infos:
        print(i)
