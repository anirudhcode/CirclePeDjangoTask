from rest_framework.views import APIView
from .models import Planets
from rest_framework import status
from rest_framework.response import Response
from .serializers import PlanetsSerializer
from inventory.models import Inventory
from django.utils import timezone
from trades.models import Trade
from django.db.models import Sum
class PlanetListView(APIView):
    def get(self, request):
        try:
            planets = Planets.objects.all()
            serializer = PlanetsSerializer(planets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class PlanetInventoryView(APIView):
    def get(self, request, id):
        try:
            planet = Planets.objects.get(id=id)
        except Planets.DoesNotExist:
            return Response({"message": "Planet not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        inventory_data = (
            Inventory.objects
            .filter(spacestation__planet=planet)
            .select_related('spacestation') 
            .values(
                'spacestation__name',
                'productName',
                'description',
                'quantity',
                'updated_at'
            )
        )

        inventory_data = [
            {
                'space_station': item.pop('spacestation__name'),
                **item
            }
            for item in inventory_data
        ]
        return Response(inventory_data, status=status.HTTP_200_OK)
    
class LowInventoryView(APIView):
    def get(self, request):
        try:
            all_inventory = Inventory.objects.all()
            low_inventory = [item for item in all_inventory if item.is_low]

            if low_inventory:
                inventory_data = [{
                    'space_station': item.spacestation.name,
                    'productName': item.productName,
                    'description': item.description,
                    'quantity': item.quantity,
                    'updated_at': item.updated_at
                } for item in low_inventory]
                
                return Response(inventory_data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No low inventory items found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

            
class PlanetTradeDataView(APIView):
    def get(self, request):
        try:
            now = timezone.now()
            last_30_days = now - timezone.timedelta(days=30)
            
            trade_data = []
            
            planets = Planets.objects.all()

            for planet in planets:
                total_trade_volume = Trade.objects.filter(
                    created_at__gte=last_30_days,
                    seller__planet=planet
                ).aggregate(total_volume=Sum('cargo__weight'))['total_volume'] or 0
                
                trade_data.append({
                    'planet': planet.localName,
                    'total_trade_volume': total_trade_volume,
                })
            return Response(trade_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)