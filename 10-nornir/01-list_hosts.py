#!/usr/bin/env python

from nornir import InitNornir

nr = InitNornir(
    config_file="nornir.yaml"
)
# list hosts
print(nr.inventory.hosts)
hosts = nr.inventory.hosts
#
# # hosts是一个特殊的对象，类似字典的方法，key值是host的字符串，value是一个内置的类host
# for hostname, host_obj in hosts.items():
#     print('hostname, type(hostname):', hostname, type(hostname))
#     print('host_obj, type(host_obj):', host_obj, type(host_obj))
#     print('host_obj.hostname:', host_obj.hostname)
#     print('host_obj.username:', host_obj.username)
#     print('host_obj.data：', host_obj.data)

# list groups
print(nr.inventory.groups)

# groups类似hosts 是一个特殊的对象
groups = nr.inventory.groups
for group_name, group_obj in groups.items():
    print(group_name, type(group_name))
    print(group_obj, type(group_obj))

# ####################################################
# #       使用我们自己的配置文件，加载自己的资产管理         #
# ####################################################
# from nornir.core.plugins.inventory import InventoryPluginRegister
#
# from plugins.inventory.cmdb_inventory import CMDBInventory
#
# InventoryPluginRegister.register("CMDBInventory", CMDBInventory)
# from nornir import InitNornir
#
# nr = InitNornir(
#     config_file="my_custom_inventory.yaml"
# )
# # list hosts
# print(nr.inventory.hosts)
# hosts = nr.inventory.hosts

import netmiko