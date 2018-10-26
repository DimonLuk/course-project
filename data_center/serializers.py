from rest_framework import serializers
from .models import Warranty, Trunk, MotherBoard


class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'


class TrunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trunk
        fields = '__all__'


class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = '__all__'
