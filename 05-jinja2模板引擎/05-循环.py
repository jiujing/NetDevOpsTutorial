from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    '''
    {% for item  in  items %}
    <对item的使用>
    {% endfor %}
    '''

    for_display = '''{% for interface in interfaces %}
端口名称是 {{ interface }}
{% endfor %}'''
    interfaces = ['eth1/1', 'eth1/2', 'eht1/3']
    template = Template(for_display)
    output = template.render(interfaces=interfaces)
    print(output)

