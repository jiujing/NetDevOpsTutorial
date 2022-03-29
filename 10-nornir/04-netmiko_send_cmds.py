from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister

from plugins.inventory.cmdb_inventory import CMDBInventory

InventoryPluginRegister.register("CMDBInventory", CMDBInventory)
nr = InitNornir(
    config_file="my_custom_inventory.yaml"
)


def show_cmds(task):
    # cmds = task.host.data['cmds']
    loop_delay_default = 0.2
    exec_timeout = 60*3
    max_loops = int(int(exec_timeout)/loop_delay_default)
    cmds = ['show runn']
    outputs = []
    for cmd in cmds:
        result = task.run(netmiko_send_command, command_string=cmd, max_loops=max_loops)
        output = result.result
        outputs.append(output)
    return outputs[0]

# dev = nr.filter(role='spine')
results = nr.run(task=show_cmds)
print_result(results)
