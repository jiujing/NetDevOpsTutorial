'''
@author: netdevops加油站 
@project: ZetCore
@file: serializers.py
@time: 2020/01/20 15:53
@desc:
'''
from rest_framework import serializers

from cmdb.models import Arp, Device


class ArpSerializer(serializers.ModelSerializer):
    dev_ip = serializers.CharField(source='device.ip')
    dev_name = serializers.CharField(source='device.name')
    extra = serializers.SerializerMethodField(
        read_only=True)  # 加括号(method_name='get_extra'),可以自行指定，系统也会根据field的name自动生成一个get_{field_name}的函

    def get_extra(self, obj):  # 会把对象传进去 方便根据一些参数计算。
        return 100

    class Meta:
        model = Arp  # 关联相关的model
        fields = '__all__'  # 可以写作 fields = ['id','intf'] 按需展示字段，也可以写作字符串'__all__'
        # exclude = ('mac',)# exclude 为不展示的字段名，和 fields 不能同时设置
        read_only_fields = ('id', 'dev_ip')
        # depth = 1  # 序列化深度指定，默认为0，建议在0-10，可以深度序列化表字段数据


def custom_validate_name(name):
    if '_' in name:
        raise serializers.ValidationError('设备名称不允许使用下划线')
        return name

def custom_validate_u(u):
    if u==10:
        raise serializers.ValidationError('此U位被保留')
        return u
class DeviceSerializer(serializers.ModelSerializer):
    # # 根据字段名，自动校验
    # def validate_name(self, name):
    #     if '_' in name:
    #         raise serializers.ValidationError('设备名称不允许使用下划线')
    #         return name

    # # 方法二，自定义校验方法，校验单个字段
    # name = serializers.CharField(max_length=32, validators=[custom_validate_name, ])  # 这个可以是多个校验函数，但是不是在对象内部，请注意

    #  #方法三 一次性校验多个字段
    # def validate(self, attrs):  # 也可以重写这个函数，校验所有字段1寸a
    #     if '_' not in attrs.get('name'):
    #         return attrs
    #     else:
    #         raise serializers.ValidationError('设备名称不允许使用下划线')

    class Meta:
        model = Device  # 关联相关的model
        fields = '__all__'  # 可以写作 fields = ['id','intf'] 按需展示字段，也可以写作字符串'__all__'
        # exclude = ('mac',)  # exclude 为不展示的字段名，和 fields 不能同时设置
        read_only_fields = ('id',)
        extra_kwargs = {
            'start_u': {
                'required': True,
                'max_value': 42,
                'min_value': 1,
                'validators': [custom_validate_u],
                'error_messages': {
                    'max_value': '1-42',
                    'min_value': '1-42',
                    'required': 'u不能为空',
                    "does_not_exist": '"{pk_value}"对应的tag对象不存在。'
                }
            }
        }
