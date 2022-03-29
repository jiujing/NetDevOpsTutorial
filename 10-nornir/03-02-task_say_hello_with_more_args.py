from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_utils.plugins.functions import print_result
import logging

nr = InitNornir(
    config_file="nornir.yaml"
)


# 创建一个nornir可以调用的task函数, 官方对于类型注解使用的比较多，比较严谨。task是一个Task的对象，返回的是一个Result的对象
def say_hello(task: Task, dev_type: str = '', sth: str = '') -> Result:
    """
    让每台设备来和大家打个招呼
    :param sth: 添加的额外参数，额外要说的话
    :param dev_type: 添加的额外参数，设备种类
    :param task: 必须有一个参数是task 且在第一个，用于上下文相关信息的管理，比如设备信息，nornir的配置等等

    :return:返回打招呼的字符串
    """
    # 添加一段额外的逻辑，纯粹为了演示，在task里，我们可以实现比较复杂的逻辑
    1/0
    if 'spine' in task.host.name:
        sth = f'{sth},and I\'m a spine'
    words = f"Hello!I'm a network dev of {dev_type}. My name is {task.host.name}.{sth}"

    return Result(
        host=task.host,  # 当前这个执行结果的设备信息
        result=words,  # 执行结果，可以是任意python对象，最终都会以str的方式打印出来，但是不影响我们取出相关信息做一些判断之类的
        # severity_level=logging.DEBUG, # log的level
    )


# 使用Nornir对象的实例nr调用run函数。
# 第一个参数task赋值成我们自己写的task函数say_hello。
# 第二个参数name是输出时比较易读准备的。可有可无
# 第三个参数是我们自己定义的设备类型
# 第四个参数是我们定义的额外要说的话
results = nr.run(task=say_hello,
                 name='A task for saying hi with more args!',
                 dev_type='switch',
                 sth='let\'s learn nornir!')

# 安装nornir_utils，调用它的打印函数，打印的效果和ansible很像。
# 但是注意，当你看到这个过程的时候，这段task实际上已经执行结束了
print_result(results)
