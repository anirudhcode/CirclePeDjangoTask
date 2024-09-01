from rest_framework.views import APIView
from rest_framework.response import Response
from inventory.models import Inventory
from django.db import models
from rest_framework import status

class StationInventoryView(APIView):
    def get(self, request, stationId):
        try:
            inventory = inventory.objects.filter(spacestation=stationId)
            if not inventory.exists():
                return Response({"message": "Inventory not found"}, status=404)
            summary = inventory.values('productName').annotate(total_quantity=models.Sum('quantity'))

            return Response(summary, status=status.HTTP_200_OK)
        except Inventory.DoesNotExist:
            return Response({"message": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)