from django.db import models


''':
datetimefield 
auto_now=Ture，字段保存时会自动保存当前时间，但要注意每次对其实例执行save()的时候都会将当前时间保存，也就是不能再手动给它存非当前时间的值。
auto_now_add=True，字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值。但是之后的save()是可以手动赋值的。也就是新实例化一个model，想手动存其他时间，就需要对该实例save()之后赋值然后再save()。

'''
# Create your models here.
class Device(models.Model):
    ip = models.CharField(verbose_name='IP地址（fqdn）',max_length=128)
    name = models.CharField(verbose_name='设备名', max_length=128)
    vendor = models.CharField(verbose_name='厂商', max_length=128)
    platform = models.CharField(verbose_name='平台(netmiko)',max_length=128)
    model = models.CharField(verbose_name='型号',max_length=128)
    series = models.CharField(verbose_name='系列',max_length=128)
    # start_u = models.IntegerField('开始U位')
    # end_u = models.IntegerField('结束U位')
    usernmae = models.CharField(verbose_name='用户名', max_length=128)
    password = models.CharField(verbose_name='密码', max_length=128)
    port = models.IntegerField(verbose_name='ssh端口',default=22)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)

    def __str__(self):
        return '{}_{}'.format(self.ip, self.name)


class Arp(models.Model):
    ip = models.CharField(verbose_name='IP', max_length=128)
    mac = models.CharField(verbose_name='mac', max_length=128)
    intf = models.CharField(verbose_name='端口', max_length=128)
    device = models.ForeignKey(Device,verbose_name='设备',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return '{}_{}'.format(self.ip, self.intf)
