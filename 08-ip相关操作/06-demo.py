from netaddr import IPSet,IPNetwork
ip_set1 = IPSet(['10.0.4.0/24'])
ip_set2 = IPSet(['10.0.4.0/28','10.0.1.0/28'])
# 用交集去计算，两个网段有没有重合
common = ip_set2&ip_set1
print(common)
if common:
    print('有重合的网段')
else:
    print('无重合的网段')