from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    '''
    {% if  condition1 %}
    <条件1为真时的逻辑>
    {% elif condition2 %} 此条可选
    <条件2为真时的逻辑> 可以继续有条件3 4 5 6 
    {% else %}
    <其他情况的逻辑>
    {% endif %} endif 一定要有，其他的elif else根据情况自己设计
    '''

    if_display = '''
    端口：{{ intf }}
    {% if status == 'up'  %}
    端口状态：'up'
    {% elif  status == 'down' %}
    端口状态：'down'
    {% else %}
    端口状态：未知
    {% endif %}
    '''

    template = Template(if_display)
    output = template.render(intf='eth1/4 ', status='up')
    print(output)

    template = get_jinja2_template('单个端口配置4if.j2')
    intf = {
        'name': 'eth1/1',
        'shutdown': True,
    }
    output = template.render(interface=intf)
    print(output)
