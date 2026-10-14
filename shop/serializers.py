from rest_framework import serializers
from .models import Flower, Payment, ArrangementType, Buyer

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ArrangementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArrangementType
        fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'