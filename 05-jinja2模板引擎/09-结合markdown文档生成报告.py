from utils import get_jinja2_template

if __name__ == '__main__':
    '''
    markdwon语法是一种文本编辑的语法，通过一些符号结合软件可以把普通文本变为富文本。
    jinja2是普通文本的模板引擎，二者结合，就可以生成一个比较生动的报告。
    markdown语法可以参考https://www.runoob.com/markdown/md-tutorial.html
    '''
    template = get_jinja2_template('report.j2')
    output = template.render(sum_of_devs=12)
    with open('report.md',mode='w',encoding='utf8') as f:
        f.write(output)