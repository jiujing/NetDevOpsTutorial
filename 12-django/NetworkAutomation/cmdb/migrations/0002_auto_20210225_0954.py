# Generated by Django 3.1.7 on 2021-02-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='ip',
            field=models.CharField(max_length=128, verbose_name='IP地址'),
        ),
    ]
