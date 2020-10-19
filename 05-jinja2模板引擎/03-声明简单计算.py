from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    # 数字的加减乘除取整取余 +-*/ // %
    template = Template('{{a + b}}')

    output = template.render(a=1, b=2)
    print(output)

    template = Template('{{a // b}}')
    output = template.render(a=1, b=2)
    print(output)

    # 字符串的计算
    template = Template('{{a +b}}')
    output = template.render(a='hello ', b='world')
    print(output)

    template = Template('{{ a*30 }}')
    output = template.render(a='=')
    print(output)

    #  比较 == >= <=  < > != 与python一致
    template = Template('{{a == b}}')
    output = template.render(a='hello ', b='world')
    print(output)

    template = Template('{{a >= b}}')
    output = template.render(a=1, b=3)
    print(output)


