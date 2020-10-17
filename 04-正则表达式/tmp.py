import re


def get_log(file):
    '''
    读取log内容，将所有\r\n替换为\n
    :param file: 文件路径
    :return: log内容
    '''
    with open(file,mode='r',encoding='utf8') as f:
        log_content = f.read()
        log_content = log_content.replace('\r\n','\n')
        return log_content

if __name__ == '__main__':
    log = get_log('show_interface.log')
    # '''编写正则表达式，构建re对象
    # re.S 代表的是. 可以匹配任意字符包括换行
    # '''
    # software_re = re.compile(r'\s+NXOS:\s+version\s+(\S+)')
    # software_re_search = software_re.search(log)
    # if software_re_search:
    #     ver = software_re_search.group(1)
    #     print(ver)
    intf_re = re.compile(r'Ethernet\d+/\d+.+?\n\n',re.S)
    intfs = intf_re.findall(log)
    print(intfs)
