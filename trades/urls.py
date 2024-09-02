from django.urls import path
from .views import TradeCreateRetrieveUpdateView, OrderDeliveredView, OrderCancelledView, PaymentConfirmView

urlpatterns = [
    path('', TradeCreateRetrieveUpdateView.as_view()),
    path('<uuid:trade_id>/', TradeCreateRetrieveUpdateView.as_view()),
    path('delivered/<uuid:id>/', OrderDeliveredView.as_view()),
    path('status/<uuid:id>/', OrderDeliveredView.as_view()),
    path('cancel/<uuid:id>/', OrderCancelledView.as_view()),
    path('confirmPayment/<uuid:id>/', PaymentConfirmView.as_view()),
]
