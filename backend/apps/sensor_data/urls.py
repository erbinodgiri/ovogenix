from django.urls import path
from .views import SensorDataCreateView, SensorDataListView, SensorDataUpdateView

urlpatterns = [
    path('', SensorDataCreateView.as_view(), name='sensor_data_create'),
    path('<int:device_id>/', SensorDataListView.as_view(), name='sensor_data_list'),
    path('<int:device_id>/update/', SensorDataUpdateView.as_view(), name='sensor_data_update'),
]