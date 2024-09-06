from django.urls import path
from .views import PlanetListView, PlanetInventoryView, LowInventoryView, PlanetTradeDataView, PlanetSummaryView

urlpatterns = [
    path('', PlanetListView.as_view(), name='planet_list'),
    path('<uuid:id>/', PlanetInventoryView.as_view(), name='planet_detail'),
    path('low-inventory/', LowInventoryView.as_view(), name='low_inventory'),
    path('trade-data/', PlanetTradeDataView.as_view(), name='trade_data'),
    path('all/', PlanetSummaryView.as_view(), name='all_planets'),
]
