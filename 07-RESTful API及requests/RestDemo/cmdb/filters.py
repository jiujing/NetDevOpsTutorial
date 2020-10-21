import django_filters
from cmdb.models import Device
from django_filters import rest_framework as filters


# 最基础的方法
# class DeviceFilter(filters.FilterSet):
#   class Meta:
#     model = Device # 指明筛选的对象
#     fields = ['name',] # 配置筛选的字段 会覆盖viewset 中的filter_fields


# # 进阶
# class DeviceFilter(django_filters.FilterSet):
#     sort = django_filters.OrderingFilter(fields=('update_time',))  # 添加排序字段
#
#     # 按需增加字段，lookup_expr可以与字段名结合，这个字段就是以name__iexact字段去搜索实现，更多查询方式，与ORM的筛选一致
#     dev_name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
#     # 以上这个就会以filed_name 去查找。
#     vendor = django_filters.CharFilter(lookup_expr='iexact')
#     min_update = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='gte')
#     max_update = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='lte')
#
#     class Meta:
#         model = Device
#         fields = ['name', 'ip']  # 会添加model的这些字段 ，与自定义字段名称冲突的以自定义字段为准
#

# 快速简单的生成复杂字段筛选
class DeviceFilter(filters.FilterSet):
    class Meta:
        model = Device  # 指明筛选的对象
        fields = {
            'update_time': ['exact','lt', 'gt'],
            'vendor': ['exact', 'iregex'],
        }
