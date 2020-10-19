from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    template = get_jinja2_template('report.j2')
    output = template.render(sum_of_devs=12)
    with open('report.md',mode='w',encoding='utf8') as f:
        f.write(output)