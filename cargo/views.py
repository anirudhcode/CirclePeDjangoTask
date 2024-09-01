from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cargo
from .serializers import CargoSerializer
from trades.models import Trade
from inventory.models import Inventory

class NewCargoView(APIView):
    def post(self, request):
        data = request.data
        serializer = CargoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            trade = Trade.objects.get(id=data['trade'])
            trade.cargo = serializer.instance
            trade.save()
            inventory = Inventory.objects.get(id=data['item'])
            volume = serializer.instance.volume
            inventory.volume -= volume
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request, id):
        try:
            cargo = Cargo.objects.get(id=id)
        except Cargo.DoesNotExist:
            return Response({"message": "Cargo not found"}, status=404)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=400)
        except Exception as e:
            return Response({"message": str(e)}, status=500)
        serializer = CargoSerializer(cargo)
        return Response(serializer.data)