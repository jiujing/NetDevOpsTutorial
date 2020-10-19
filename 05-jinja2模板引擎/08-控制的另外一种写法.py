from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':
    '''
    自定义控制及其他的所有符号
        block_start_string=BLOCK_START_STRING,
        block_end_string=BLOCK_END_STRING,
        variable_start_string=VARIABLE_START_STRING,
        variable_end_string=VARIABLE_END_STRING,
        comment_start_string=COMMENT_START_STRING,
        comment_end_string=COMMENT_END_STRING,
        line_statement_prefix=LINE_STATEMENT_PREFIX,
        line_comment_prefix=LINE_COMMENT_PREFIX,
        trim_blocks=TRIM_BLOCKS,
        lstrip_blocks=LSTRIP_BLOCKS,
        newline_sequence=NEWLINE_SEQUENCE,
        keep_trailing_newline=KEEP_TRAILING_NEWLINE,
        对应默认值
        # defaults for the parser / lexer
        BLOCK_START_STRING = "{%"
        BLOCK_END_STRING = "%}"
        VARIABLE_START_STRING = "{{"
        VARIABLE_END_STRING = "}}"
        COMMENT_START_STRING = "{#"
        COMMENT_END_STRING = "#}"
        LINE_STATEMENT_PREFIX = None
        LINE_COMMENT_PREFIX = None
        TRIM_BLOCKS = False
        LSTRIP_BLOCKS = False
        NEWLINE_SEQUENCE = "\n"
        KEEP_TRAILING_NEWLINE = False
    '''
    # #自定义<% %>作为逻辑控制符号
    # templ = '''
    # <% if a>b %>
    #  a>b
    # <% endif %>
    # '''
    # template = Template(templ,block_start_string='<%',block_end_string='%>')
    # output = template.render(a=40,b=10)
    # print(output)
    # # 使用# 单行控制逻辑，简洁
    templ = '''
        # if a>b
         a>b
        # endif
        '''
    template = Template(templ,  line_statement_prefix='#')
    output = template.render(a=41, b=10)
    print(output)