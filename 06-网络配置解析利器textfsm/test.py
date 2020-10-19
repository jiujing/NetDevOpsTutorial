from textfsm import TextFSM


if __name__ == '__main__':
    with open('case04.log', 'r', encoding='utf8') as f:
        dev_text = f.read()
    template = TextFSM(open('case04C.textfsm',encoding='utf8'))
    infos = template.ParseTextToDicts(dev_text)
    for i in infos:
        print(i)
        