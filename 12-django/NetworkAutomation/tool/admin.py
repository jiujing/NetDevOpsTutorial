from django.contrib import admin

from tool.utils.device_config_handler import push_config_2_device
from tool.models import  QuickOperation

def operation_action(operation: QuickOperation):
    configs = operation.cmds.splitlines()
    ip = operation.device.ip
    username = operation.device.usernmae
    password = operation.device.password
    port = operation.device.port
    result = push_config_2_device(ip=ip,username=username,password=password,port=port,configs=configs)
    success = result.get('success')
    return success



def push_open_config_2_device(modeladmin, request, queryset):
    for operation in queryset:
        success = operation_action(operation)
        operation.is_on = True if success else False
        operation.save()

push_open_config_2_device.short_description = "开启"




def push_close_config_2_device(modeladmin, request, queryset):
    for operation in queryset:
        success = operation_action(operation)
        operation.is_on = True if success else False
        operation.save()

push_close_config_2_device.short_description = "关闭"

@admin.register(QuickOperation)
class QuickOperationAdmin(admin.ModelAdmin):
    list_display = ['group', 'name', 'is_on']
    search_fields = ['group','name']
    list_per_page = 20
    actions = [push_close_config_2_device,push_open_config_2_device]
    list_filter=['group','device']