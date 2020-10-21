from rest_framework.routers import DefaultRouter
from django.urls import path
from cmdb.views import ArpViewSet, DeviceViewSet

urlpatterns = []
router = DefaultRouter()
router.register(r'arps', ArpViewSet, 'arps')  # 注册路由，处理所有arps的请求
router.register(r'devices', DeviceViewSet, 'devices')  # 注册路由，处理所有arps的请求
urlpatterns += router.urls  # router注册后自动生成若干urls 列表类型



