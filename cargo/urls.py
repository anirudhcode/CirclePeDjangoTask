from django.urls import path
from .views import NewCargoView, DeleteCargoView, CargoVolumeSummaryView, CargoStatusSummaryView, RecentCargoView \
    , AllCargoPaginationView
urlpatterns = [
    path('', NewCargoView.as_view(), name='cargo_list'),
    path('<uuid:id>/', NewCargoView.as_view(), name='cargo_detail'),
    path('<uuid:id>/delete/', DeleteCargoView.as_view(), name='cargo_delete'),
    path('volume/', CargoVolumeSummaryView.as_view(), name='cargo_volume'),
    path('delivered/', CargoStatusSummaryView.as_view(), name='cargo_delivery'),
    path('recent/', RecentCargoView.as_view(), name='recent_cargo'),
    path('all/', AllCargoPaginationView.as_view(), name='all_cargo'),
]