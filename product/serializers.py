from rest_framework import serializers
from .models import Product, RealEstate, Vehicle, Offer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    real_estate = RealEstateSerializer(required=False)
    vehicle = VehicleSerializer(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'product', 'user', 'amount', 'timestamp']

    # user = serializers.ReadOnlyField(source='user.username')
