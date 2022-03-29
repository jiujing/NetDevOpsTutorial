from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir(
    config_file="config.yaml"
)
#
# # 键值对通过F实现
beijing_devs = nr.filter(F(city='beijing'))
print(beijing_devs.inventory.hosts.keys())

# # 逻辑与 &
# beijing_leaf_devs = nr.filter(F(city='beijing') & F(role='leaf'))
# print(beijing_leaf_devs.inventory.hosts.keys())

# # 逻辑或 |
# beijing_or_spine_devs = nr.filter(F(city='beijing') | F(role='spine'))
# print(beijing_or_spine_devs.inventory.hosts.keys())
#
# # 逻辑非 ~
# beijing_and_not_leaf_devs = nr.filter(F(city='beijing') & ~F(role='leaf'))
# print(beijing_and_not_leaf_devs.inventory.hosts.keys())

# # contains 字符串包含某子串
# hostname_contains_192_devs = nr.filter(F(hostname__contains='192'))
# print(hostname_contains_192_devs.inventory.hosts.keys())
#
# # # contans list包含某元素
# netdevops_devs = nr.filter(F(groups__contains='netdevops'))
# print(netdevops_devs.inventory.hosts.keys())

# # # contans dict包含某key
# with_model_info_devs = nr.filter(F(info__contains='model'))
# print(with_model_info_devs.inventory.hosts.keys())

# # 嵌套的数据层层取值，每次用双下划线进行一次下钻,可以多次下钻，下钻后根据情况进行判断，是用contains还是直接用等号判断

# nested_demo_devs = nr.filter(F(nonsense_dict__a=1))
# print(nested_demo_devs.inventory.hosts.keys())

# nested_demo_devs = nr.filter(F(nonsense_dict__b_dict__nums__contains=1))
# print(nested_demo_devs.inventory.hosts.keys())