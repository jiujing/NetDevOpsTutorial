from ntc_templates.parse import parse_output

if __name__ == "__main__":
    '''
    parse_output三个参数
    platform 对应netmiko的device_type
    command 你执行的命令，可以缩写
    data show回来的结果（文本，字符串）
    返回字典的list
    '''
    with open('show_interface_brief.log', 'r', encoding='utf8') as f:
        raw_config_text = f.read()
    datas = parse_output(platform='cisco_ios', command='show ip int bri', data=raw_config_text)
    for i in datas:
        print(i)



