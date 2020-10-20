from textfsm import TextFSM


if __name__ == '__main__':
    with open('show_version.log', 'r', encoding='utf8') as f:
        dev_text = f.read()
    template = TextFSM(open('show_version_easy.textfsm',encoding='utf-8'))
    version_info = template.ParseTextToDicts(dev_text)

    print(version_info)
