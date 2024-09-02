from django.urls import path
from .views import AddItemView, DeleteItemView
from django.urls.conf import include

urlpatterns = [
    path('', include('spacestations.urls')),
    path('add-item/', AddItemView.as_view(), name='add_item'),
    path('delete-item/', DeleteItemView.as_view(), name='delete_item'),
]