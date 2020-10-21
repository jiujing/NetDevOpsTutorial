from cmdb.models import Arp, Device
from cmdb.serializers import ArpSerializer, DeviceSerializer
from rest_framework.viewsets import ModelViewSet
from cmdb.filters import DeviceFilter

class ArpViewSet(ModelViewSet):
    queryset = Arp.objects.all()
    serializer_class = ArpSerializer
    filter_fields = '__all__'


class DeviceViewSet(ModelViewSet):
    """
    retrieve:
        Return a device instance,获取device单设备的详细信息.
    list:
        Return all devices, ordered by most recently joined.
    create:
        Create a new device.
    delete:
        Remove an existing device.
    partial update:
        Update one or more fields on an existing device.
    update:
        Update a device.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_class = DeviceFilter
    # filter_fields = ['name','vendor'] # '__all__' # 会被filter_class里的fileds覆盖

    # 重写GenericAPIView下的该方法,以实现自己对query_set的返回加一些逻辑
    # 比如曾加筛选或者是按用户返回指定数据
    # def get_queryset(self):
    #     vendor = self.request.query_params.get("vendor")
    #     name = self.request.query_params.get("name")
    #     if vendor:
    #         self.queryset = self.queryset.filter(vendor=vendor)
    #     if name:
    #         self.queryset = self.queryset.filter(name=name)
    #     return self.queryset
