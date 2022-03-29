from nornir import InitNornir

nr = InitNornir(
    config_file="config.yaml"
)

# # 简单匹配筛选，单字段
# huawei_devs = nr.filter(platform='huawei')
# print(huawei_devs.inventory.hosts)
#
# # 简单匹配筛选，多字段
# huawei_devs = nr.filter(platform='huawei', port=22)
# print('huawei devs:', huawei_devs.inventory.hosts)
#
# # 对data内字段的筛选，直接可以使用data对应字段进行筛选
# bj_devs = nr.filter(city='beijing')
# print('bj_devs:', bj_devs.inventory.hosts)

# spine_devs = nr.filter(role='spine')
# print('spine devs:', spine_devs.inventory.hosts)
#
# bj_spine_devs = nr.filter(role='spine', city='beijing')
# print('bj_spine_devs:', bj_spine_devs.inventory.hosts)

# # 链式调用，俄罗斯套娃式调用，每次filter会返回一个nornir对象，所以我们实际是可以链式调用的
# huawei_devs = nr.filter(platform='huawei', port=22)
# chain1_devs = huawei_devs.filter(city='beijing')
# print('chain1 devs: ', chain1_devs.inventory.hosts)
# chain2_devs = huawei_devs.filter(username='netdevops').filter(hostname='192.168.56.209')
# print('chain2 devs hosts: ', chain2_devs.inventory.hosts)
# print('chain2 devs: ', chain2_devs)


# # 自定义函数调用
# def beijing_leaf_filter(host):  # 传入一个host参数，这是每台主机的Host对象，nornir会循环判断
#     if host['role'] == 'leaf' and host['city'] == 'beijing':
#         return True  # 最终返回True or False。True代表设备符合要求
#     return False
#
#
# bj_leaf_devs = nr.filter(filter_func=beijing_leaf_filter)  # 直接将函数名称赋值给filter_func这个参数即可
# print('bj_leaf_devs filter by func:', bj_leaf_devs.inventory.hosts)


# # 隶属于某个group的主机清单
#
# netdevops_devs = nr.inventory.children_of_group('netdevops')
# print(netdevops_devs, type(netdevops_devs))

# 链式调用
#
# leaves = nr.filter(F(name__contains='leaf'))
# print(leaves.inventory.hosts)
