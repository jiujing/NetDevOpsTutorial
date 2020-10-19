from jinja2 import Template

if __name__ == '__main__':
    template = Template('Hello {{ name }}!')
    output = template.render(name='John Doe')
    print(output)
    # intf_templ = '''
    # config
    # interface {{ intf_name}}
    #     description {{ desc }}
    # no shutdown
    # '''
