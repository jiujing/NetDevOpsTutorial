from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result

nr = InitNornir(
    config_file="nornir.yaml"
)




dev02 = nr.inventory.hosts['dev02.leaf']
print(dev02,type(dev02))
print(dev02.hostname,dev02.platform)
print(dev02['tags'],dev02['cmds'])


def hi(task):
    words = f"Hi!I'm a network device. My name is {task.host.name}"
    try:
        for group in task.host.groups:
            if group.groups:
                print('group {}  has groups：{}'.format(group, group.groups))
            else:
                print('group {}  has no groups,{} '.format(group, group.groups))
    except:
        print()
    return words


results = nr.run(task=hi, name='A task for saying hi!')

print_result(results)

# results = nr.run(task=say, sth='hello world!')
# def say(task, sth):
#     words = f"Hi!I'm a network device. My name is {task.host.name}, {sth}"
