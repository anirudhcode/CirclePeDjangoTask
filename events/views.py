from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Events
from .serializers import EventsSerializer

class EventListPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class EventListView(APIView):
    pagination_class = EventListPagination
    def get(self, request):
        events = Events.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(events, request)
        serializer = EventsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)