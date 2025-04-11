from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/devices/', include('apps.devices.urls')),
    path('api/sensor-data/', include('apps.sensor_data.urls')),
    path('api/alerts/', include('apps.alerts.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
    path('api/machine-observations/', include('apps.machine_observation_data.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]