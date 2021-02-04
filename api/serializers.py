from rest_framework import serializers
from .models import *
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class ActorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Actor
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"


class Adress_distributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress_distributor
        fields = "__all__"


class SeedCategorySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = SeedCategory
        fields = "__all__"

class VarietySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Variety
        fields = "__all__"


class RateSeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateSeed
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = "__all__"


class SeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seed
        fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = "__all__"