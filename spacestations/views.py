from rest_framework.views import APIView
from rest_framework.response import Response
from inventory.models import Inventory
from rest_framework import status
from inventory.serializers import SpaceStationInventorySerializer
from spacestations.serializers import SpaceStationsSerializer
from spacestations.models import SpaceStations
from django.core.paginator import Paginator

class StationInventoryView(APIView):
    def get(self, request, stationId):
        try:
            inventory = Inventory.objects.filter(spacestation=stationId)
            serializer = SpaceStationInventorySerializer(inventory, many=True)
            return Response(serializer.data)
        except Inventory.DoesNotExist:
            return Response({"message": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StationDetailsView(APIView):
    def get(self, request, stationId):
        try:
            print(stationId)
            station = SpaceStations.objects.get(id=stationId)
        except SpaceStations.DoesNotExist:
            return Response({"message": "Space Station not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = SpaceStationsSerializer(station)
        return Response(serializer.data)

class StationListPaginationView(APIView):
    def get(self, request):
        try:
            stations = SpaceStations.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(stations, 5)
            serializer = SpaceStationsSerializer(paginator.page(page), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)