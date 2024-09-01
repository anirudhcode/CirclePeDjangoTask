from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('trades/', include('trades.urls')),
]