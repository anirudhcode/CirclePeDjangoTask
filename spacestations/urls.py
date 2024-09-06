from django.urls import path
from .views import StationInventoryView, StationDetailsView, StationListPaginationView

urlpatterns = [
    path('<uuid:stationId>/', StationInventoryView.as_view(), name='station_inventory'),
    path('<uuid:stationId>/details/', StationDetailsView.as_view(), name='station_detail'),
    path('all/', StationListPaginationView.as_view(), name='all_stations'),
]
