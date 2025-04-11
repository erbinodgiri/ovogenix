from django.urls import path
from .views import DataSummaryView, AlertsSummaryView

urlpatterns = [
    path('data-summary/', DataSummaryView.as_view(), name='data_summary'),
    path('alerts-summary/', AlertsSummaryView.as_view(), name='alerts_summary'),
]