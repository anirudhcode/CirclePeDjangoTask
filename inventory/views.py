from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inventory
from rest_framework import status
from .serializers import InventorySerializer

class AddItemView(APIView):
    def post(self, request):
        data = request.data
        if 'id' in data:
            inventory = Inventory.objects.get(id=data['id'])
            inventory.quantity += data['quantity']
            inventory.save()
            return Response({"message": "Item added successfully"}, status=status.HTTP_200_OK)
        serializer = InventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteItemView(APIView):
    def delete(self, request):
        data = request.data
        inventory = Inventory.objects.get(id=data['id'])
        if inventory.quantity < data['quantity']:
            return Response({"message": "Not enough quantity of the item in inventory"}, status=status.HTTP_400_BAD_REQUEST)
        inventory.quantity -= data['quantity']
        inventory.save()
        return Response({"message": "Item count reduced successfully successfully"}, status=status.HTTP_200_OK)