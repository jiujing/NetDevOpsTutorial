from django.shortcuts import render, HttpResponse
from cmdb.models import Device

# Create your views here.
def device_index(request):
    return HttpResponse('这是我的第一个CMDB！')


# def device_list(request):
#     devices = [
#         {'id': 1, 'name': 'dev01', 'ip': '192.168.1.2', 'vendor': 'huawei', 'is_virtual': False},
#         {'id': 2, 'name': 'dev02', 'ip': '192.168.1.5', 'vendor': 'h3c', 'is_virtual': False},
#         {'id': 3, 'name': 'dev03', 'ip': '192.168.1.7', 'vendor': 'hillstone', 'is_virtual': True},
#     ]
#     return render(request, 'device/device_list.html', {'devices': devices})


# orm mode
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device/device_list.html', {'devices': devices})