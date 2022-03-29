# Generated by Django 3.1.7 on 2021-02-24 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('group', models.CharField(choices=[('运维VPN开通', '运维VPN开通'), ('生物岛ECC网络开通', '生物岛ECC网络开通')], max_length=128, verbose_name='分组')),
                ('cmds', models.TextField(verbose_name='下发命令')),
                ('is_on', models.BooleanField(default=True, verbose_name='开启状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.device', verbose_name='操作设备')),
            ],
        ),
    ]
