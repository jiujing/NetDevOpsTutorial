from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_utils.plugins.functions import print_result
from netmiko import Netmiko
import logging

nr = InitNornir(
    config_file="nornir.yaml"
)


# 创建一个nornir可以调用的task函数, 官方对于类型注解使用的比较多，比较严谨。task是一个Task的对象，返回的是一个Result的对象
def say_sth(task: Task, sth: str = '') -> Result:
    """
    让每台设备来和大家打个招呼
    :param sth: 添加的额外参数，额外要说的话
    :param task: 必须有一个参数是task 且在第一个，用于上下文相关信息的管理，比如设备信息，nornir的配置等等
    :return:返回要说的字符串
    """
    words = f"{sth}!"
    return Result(host=task.host, result=words)


def show_version(task: Task):
    """
    登录设备展示version相关信息，默认执行show version，各个设备按需
    :param task:
    :param cmd:
    :return:
    """
    # 我们从task中取到待执行设备的相关信息。将和ssh登录相关的记录到dev_info，供后续netmiko使用
    host = task.host
    print(host,'开始执行命令')
    dev_info = dict(
        ip=host.hostname,
        username=host.username,
        password=host.password,
        port=host.port,
        device_type=host.platform
    )

    # 再从data中获取展示version的命令
    # 如无使用默认值，或者我们也可以在这个地方根据device_type做一个mapping，我觉得可能更简单。
    cmd = host.data.get('show_version_cmd', 'show version')
    print(dev_info, 'dev_info')
    # with 创建连接，并执行命令
    with Netmiko(**dev_info) as dev_conn:
        output = dev_conn.send_command(cmd)

    # 将执行命令的回显放到output变量中后创建一个Nornir所需的执行结果Result对象
    return Result(host=task.host, result=output)


def grouping_task_demo(task, before, after):
    """
    先说你好，show version后，说再见
    :param task: task上下文，必填
    :param before: 先说的话
    :param after: 后说的话
    :return: 返回结果可以为空，也可以根据每个结果来进行一个逻辑判断后返回执行结果。
             此处我们简单一点，返回空。
    """
    # 使用task上下文变量，调用它的run函数，传入的参数task是要执行的task函数，name是为了方便阅读，其他参数按照task函数，按需填入。
    # 打招呼
    task.run(name='before show version', task=say_sth, sth=before)

    # 执行show_version的函数，返回version文本，print_results会帮我们自动处理子task函数的结果显示
    task.run(name='my version info is:', task=show_version)
    task.run(name='after show version', task=say_sth, sth=after)
    return Result(host=task.host, result='我们执行了一套组合task')


# 使用Nornir对象的实例nr调用run函数。
# 第一个参数task赋值成我们自己写的task函数say_sth。
# 第二个参数name是输出时比较易读准备的。可有可无
# 第三个参数是我们自己定义的设备类型
# 第四个参数是我们定义的额外要说的话
before = 'nice to meet u'
after = 'bye'
cmd = 'show verison'
results = nr.run(task=grouping_task_demo,
                 name='I\'m a grouping_task_demo !',
                 before=before,
                 after=after)

# 安装nornir_utils，调用它的打印函数，打印的效果和ansible很像。
# 但是注意，当你看到这个过程的时候，这段task实际上已经执行结束了
print_result(results)
