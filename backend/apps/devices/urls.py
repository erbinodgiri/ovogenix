from django.urls import path
from .views import DeviceRegistrationView, DeviceListView

urlpatterns = [
    path('register/', DeviceRegistrationView.as_view(), name='device_register'),
    path('', DeviceListView.as_view(), name='device_list'),
]