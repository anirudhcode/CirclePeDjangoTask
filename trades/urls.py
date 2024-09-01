from django.urls import path
from .views import TradeCreateRetrieveUpdateView

urlpatterns = [
    path('trades/', TradeCreateRetrieveUpdateView.as_view())
]
