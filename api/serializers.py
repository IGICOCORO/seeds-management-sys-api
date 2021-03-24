from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class TokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        return data

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        exclude = "last_login","is_staff","date_joined","user_permissions"


# class ActorSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()

#     class Meta:
#         model = Actor
#         fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"


class AdressDistributorSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep['distributor'] = obj.distributor.username
        return rep  

    class Meta:
        model = AdressDistributor
        fields = "__all__"


class VarietySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Variety
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = "__all__"


class SeedSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep['nom'] = obj.nom.nom
        rep['variety'] = obj.variety.nom
        return rep  

    class Meta:
        model = Seed
        fields = '__all__'


# class CommandeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Commande
#         fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Stock
        fields = "__all__"
        depth =1