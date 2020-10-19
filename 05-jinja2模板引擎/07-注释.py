from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':

    '''
    {# ... #} 用来进行注释
    通过注释，我们可以让别人比较容易的读懂我们的模板
    '''

    templ = '''{# 这是一个注释行，不会被输出 #}
这是用来演示注释的，你看不到{# ... #}内的注释的内容'''
    template = Template(templ)
    output = template.render()
    print(output)

    '''
    实例化template的时候，我们可以赋值line_comment_prefix='我们想要的单行注释符号'
    实现单行的注释
    '''
    templ = '''#这是一个注释行，不会被输出，因为我们赋值了line_comment_prefix='#'
    这是用来演示单行注释的，你看不到{{ '#' }}之后的注释的内容 #这是一个注释行，不会被输出，因为我们赋值了line_comment_prefix='#' '''
    # template = Template(templ, line_comment_prefix='#')
    template = Template(templ, line_comment_prefix='#')
    output = template.render()
    print(output)
