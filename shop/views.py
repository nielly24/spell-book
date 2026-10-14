from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Flower, Payment, ArrangementType, Buyer
from .serializers import FlowerSerializer, PaymentSerializer, ArrangementTypeSerializer, BuyerSerializer

class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAuthenticated] 

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class ArrangementTypeViewSet(viewsets.ModelViewSet):
    queryset = ArrangementType.objects.all()
    serializer_class = ArrangementTypeSerializer
    permission_classes = [IsAuthenticated]

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [IsAuthenticated]