from django.urls import path
from .views import AlertListView, AlertResolveView

urlpatterns = [
    path('', AlertListView.as_view(), name='alert_list'),
    path('<int:alert_id>/resolve/', AlertResolveView.as_view(), name='alert_resolve'),
]