from jinja2 import Template


def get_jinja2_template(file):
    with open(file,mode='r', encoding='utf8') as f:
        return Template(f.read())
