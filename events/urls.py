from django.urls import path
from .views import EventListView

urlpatterns = [
    path('real-time/', EventListView.as_view(), name='real_time'),
]
