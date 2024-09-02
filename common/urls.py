from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('trades/', include('trades.urls')),
    path('events/', include('events.urls')),
    path('spacestations/', include('spacestations.urls')),
    path('inventory/', include('inventory.urls')),
    path('planets/', include('planets.urls')),
    path('cargo/', include('cargo.urls')),
    path('updates/', include('events.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]