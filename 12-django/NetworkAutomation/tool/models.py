from django.db import models
from  cmdb.models import Device

group_choices = (('运维VPN开通','运维VPN开通'),('生物岛ECC网络开通','生物岛ECC网络开通'))
# Create your models here.
class QuickOperation(models.Model):
    name = models.CharField(verbose_name='名称', max_length=128)
    group = models.CharField(verbose_name='分组',choices=group_choices, max_length=128)
    # start_u = models.IntegerField('开始U位')
    # end_u = models.IntegerField('结束U位')
    device = models.ForeignKey(Device,verbose_name='操作设备',on_delete=models.SET_NULL,null=True)
    cmds = models.TextField(verbose_name='下发命令')
    is_on = models.BooleanField(verbose_name='开启状态',default=True) 
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)

    def __str__(self):
        return self.name


# class Arp(models.Model):
#     ip = models.CharField(verbose_name='IP', max_length=128)
#     mac = models.CharField(verbose_name='mac', max_length=128)
#     intf = models.CharField(verbose_name='端口', max_length=128)
#     device = models.ForeignKey(Device,verbose_name='设备',on_delete=models.CASCADE,null=True,blank=True)

#     def __str__(self):
#         return '{}_{}'.format(self.ip, self.intf)
