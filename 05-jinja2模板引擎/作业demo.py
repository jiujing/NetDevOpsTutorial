from jinja2 import Template
import pandas as pd


def read_templ_from_file(file, encoding='utf8'):
    with open(file, mode='r', encoding=encoding) as f:
        text = f.read()
        templ = Template(text)
        return templ


def read_datas_from_excel(file):
    dataframe = pd.read_excel(file)
    items = dataframe.to_dict(orient='records')
    return items


def generate_configs(templ, datas):
    configs = templ.render(datas=datas)
    return configs


if __name__ == '__main__':
    datas = read_datas_from_excel('interfaces.xlsx')
    templ = read_templ_from_file('zuoye.j2')
    configs = generate_configs(templ=templ, datas=datas)
    print(configs)
