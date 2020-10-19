from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    '''
    我们会发现，每行都多了一个换行，如果我们想去掉换行，可以使用-来控制
    - 就是去除此次控制（if for）的左侧或者右侧的空白符
    '''


    # 这段的- 在if左侧，所以会去掉if左侧的所有空白符，yay会紧紧跟随上一行的div
    templ = '''<div>
    {%- if True %}yay
{% endif %}
</div>'''
    template = Template(templ)
    output = template.render()
    print(output)

    # 这段的- 在end的左侧，所以会去掉end左侧的所有空白符，但是不会去掉右侧的空白符（换行）
    templ = '''<div>
        {%- if True %}yay
    {%- endif %}
</div>'''
    template = Template(templ)
    output = template.render()
    print(output)