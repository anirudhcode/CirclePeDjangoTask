from django.urls import path
from .views import StationInventoryView, StationDetailsView

urlpatterns = [
    path('<uuid:stationId>/', StationInventoryView.as_view(), name='station_inventory'),
    path('<uuid:stationId>/details/', StationDetailsView.as_view(), name='station_detail'),
]
