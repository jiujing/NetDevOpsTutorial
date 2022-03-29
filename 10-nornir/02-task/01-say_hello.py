from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result

nr = InitNornir(
    config_file="../nornir.yaml"
)


def hi(task):
    words = f"Hi!I'm a network device. My name is {task.host.name}"
    print('task.host.port:', task.host.port)
    print('task.host.groups:', task.host.groups)
    print('task.host.data:', task.host.data)
    return words


results = nr.run(task=hi, name='A task for saying hi!')

print_result(results)

# results = nr.run(task=say, sth='hello world!')
# def say(task, sth):
#     words = f"Hi!I'm a network device. My name is {task.host.name}, {sth}"
