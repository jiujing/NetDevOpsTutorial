from django.contrib import admin

from cmdb.models import Arp, Device


@admin.register(Arp)
class ArpAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'mac', 'intf']
    list_per_page = 20


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'name', 'vendor']
    list_per_page = 20
