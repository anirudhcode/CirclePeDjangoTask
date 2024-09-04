from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cargo
from .serializers import CargoSerializer, RecentCargoSerializer
from trades.models import Trade
from inventory.models import Inventory
from django.utils import timezone
from datetime import timedelta


class NewCargoView(APIView):
    def post(self, request):
        data = request.data
        serializer = CargoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if 'trade' in data:
                trade = Trade.objects.get(id=data['trade'])
                trade.cargo = serializer.instance
                trade.save()
            inventory = Inventory.objects.get(id=data['item'])
            volume = serializer.instance.volume
            inventory.quantity -= volume
            inventory.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request, id):
        try:
            cargo = Cargo.objects.get(id=id)
        except Cargo.DoesNotExist:
            return Response({"message": "Cargo not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = CargoSerializer(cargo)
        return Response(serializer.data)
    
class DeleteCargoView(APIView):
    def delete(self, request, id):
        cargo = Cargo.objects.get(id=id)
        trade = Trade.objects.get(cargo=cargo)
        inventory = Inventory.objects.get(id=cargo.item.id)
        volume = cargo.volume
        inventory.quantity += volume
        trade.cargo = None
        trade.save()
        cargo.delete()
        return Response({"message": "Cargo deleted successfully"}, status=status.HTTP_200_OK)


class CargoVolumeSummaryView(APIView):
    def get(self, request):
        cargo = Cargo.objects.filter(shipment_date__gte=timezone.now()-timedelta(days=30))
        return Response({"trade_volume": sum([c.volume for c in cargo])})
    
class CargoStatusSummaryView(APIView):
    def get(self, request):
        cargoShipped = Cargo.objects.filter(shipment_date__gte=timezone.now()-timedelta(days=30)).exclude(status='PENDING').count()
        totalCargo = Cargo.objects.filter(shipment_date__gte=timezone.now()-timedelta(days=30)).count()
        percentage = round((cargoShipped/totalCargo)*100, 2)
        return Response({"percentage": percentage})

class RecentCargoView(APIView):
    def get(self, request):
        cargoItems = Cargo.objects.all().order_by('-shipment_date')[:6]
        
        serializer = RecentCargoSerializer(cargoItems, many=True)
        if not serializer.data:
            return Response({"message": "No recent cargo items found"}, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)