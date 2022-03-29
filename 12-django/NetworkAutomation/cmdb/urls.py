from django.urls import path
from .views import device_list,device_index
urlpatterns = [
    path('device/index/',device_index,name='device_index'),
    path('device/list/',device_list,name='device_list'),
]
