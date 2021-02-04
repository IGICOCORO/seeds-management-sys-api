from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication
#from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import *


"""class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer"""


class ActorViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ClientViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class Adress_distributorViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Adress_distributor.objects.all()
    serializer_class = Adress_distributorSerializer


class SeedCategoryViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SeedCategory.objects.all()
    serializer_class = SeedCategorySerializer


class VarietyViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer


class CommandeViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


class RateSeedViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = RateSeed.objects.all()
    serializer_class = RateSeedSerializer


class PlantViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class SeedViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer


class StockViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer