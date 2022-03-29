from django.contrib import admin

from cmdb.models import  Device



@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    # 列表页显示那些字段（列）
    list_display = ['id', 'ip', 'name', 'vendor']

    # 点击此字段可进行跳转详情页
    list_display_links = ['id', 'ip', 'name']

    # 搜索字段
    search_fields = ['ip','name','vendor']

    # 每页显示多少条记录
    list_per_page = 20

    # 不显示字段
    # exclude = ['is_virtual']  # 不显示字段

    # 侧边过滤器
    list_filter = ['name']

    # 日期的筛选过滤 本model无，供参考
    date_hierarchy = 'created_time'

    ordering = ('ip', '-name')  # 列表页排序依据，负号代表逆序