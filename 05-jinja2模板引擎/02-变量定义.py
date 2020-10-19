from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    '''
    变量用双花括号圈起来，建议左右各留一个空格
    render的时候变量对不上不会报错
    花括号内的变量可以进行简单运算
    '''
    template = get_jinja2_template('变量展示.j2')
    '''
    以下是一个普通的数字的变量的展示
a is {{ a }}, b is {{ b }} ,and a+b = {{ a + b }}

以下是一个字符串的相关展示
Jinja2 says: {{ words }}

以下是一个list的展示
list x is {{ x_list }}

以下是一个dict的展示
dict y is {{ y_dict }}
    '''
    a = 1
    b = 3
    words = 'hello world!'
    x_list = [1, 2, 3, 4]
    y_dict = {
        'name': 'xiaoming',
        'age': 18
    }

    output = template.render(a=a, b=b, words=words, x_list=x_list, y_dict=y_dict)
    print(output)
