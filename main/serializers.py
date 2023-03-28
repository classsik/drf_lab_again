from rest_framework import serializers
from .models import Cart, Tour, Exscursion, Country


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class ExscursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exscursion
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
