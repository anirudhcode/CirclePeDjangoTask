from django.urls import path
from .views import PlanetListView, PlanetInventoryView, LowInventoryView

urlpatterns = [
    path('', PlanetListView.as_view(), name='planet_list'),
    path('<uuid:id>/', PlanetInventoryView.as_view(), name='planet_detail'),
    path('low-inventory/', LowInventoryView.as_view(), name='low_inventory'),
]
