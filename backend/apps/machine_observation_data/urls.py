from django.urls import path
from .views import MachineObservationCreateView, MachineObservationListView

urlpatterns = [
    path('', MachineObservationCreateView.as_view(), name='machine_observation_create'),
    path('<int:machine_id>/', MachineObservationListView.as_view(), name='machine_observation_list'),
]