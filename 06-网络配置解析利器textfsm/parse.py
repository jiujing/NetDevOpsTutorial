"""ntc_templates.parse."""
import os
from textfsm import TextFSM
import re


def _get_template_dir(template_dir=None):
    if not template_dir:
        package_dir = os.path.dirname(__file__)
        template_dir = os.path.join(package_dir, "templates")
    if not os.path.isdir(template_dir):
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(template_dir)))
        template_dir = os.path.join(project_dir, "templates")

    return template_dir


def get_textfsm_obj(Command, Platform,template_dir=None):
    '''
    通过设备的平台和cmd去匹配index中对应的模板
    不调用处理table，从而完成对windows的彻底兼容
    但也对文件锁等细节处理不当，但是在个人PC上演示调试不会造成太大问题。生产环境，仍然建议使用Linux部署
    '''
    Command_re_str = ' '.join(['{}{}'.format(i, '[a-zA-Z0-9]*?') for i in Command.split()])
    re_str = r'.*?{}.*? .*?{}.*?\.textfsm'.format(Platform, Command_re_str)
    re_str = re_str.replace(' ', '_').lower()
    textfsm_templ_re = re.compile(re_str)
    index_file = os.path.join(_get_template_dir(template_dir), 'index')
    with open(index_file, 'r', encoding='utf8') as f:
        index_text = f.read()
    results = textfsm_templ_re.findall(index_text)

    if results:
        # 查找所有符合的，符合的条件是最短原则，根据index文件的顺序，最短的在下方，所以取-1
        textfsm_templ_name = results[-1]
    else:
        raise Exception(f'No template found for {Command} at {Platform}:')
    textfsm_templ_iofile = open(os.path.join(_get_template_dir(), textfsm_templ_name), 'r', encoding='utf8')
    return TextFSM(textfsm_templ_iofile)


def parse_output(platform=None, command=None, data=None):
    """Return the structured data based on the output from a network device."""

    attrs = {"Command": command, "Platform": platform}
    fsm = get_textfsm_obj(**attrs)
    structured_data = fsm.ParseTextToDicts(data)
    structured_data_lower = []
    structured_data_lower = [{k.lower(): v for k, v in data.items()} for data in structured_data]
    # for data in structured_data:
    #     structured_data_lower.append(
    #         {k.lower():v for k,v in data.items()}
    #     )
    return structured_data_lower
