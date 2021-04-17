from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import *


class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer


class UserViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, JWTAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = request.data
        user = User(
            username = data.get("username"),
            email = data.get("email"),
            first_name = data.get("first_name"),
            last_name = data.get("last_name")
        )
        user.set_password("password")
        
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, 201)

    def update(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        username = data.get("username")
        if username : user.username = username
        password = data.get("password")
        if password : user.set_password(password)
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, 201)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'status': 'success'}, 204)



# class ActorViewset(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer


class ClientViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AdressDistributorViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = AdressDistributor.objects.all()
    serializer_class = AdressDistributorSerializer


class VarietyViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer


# class CommandeViewset(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Commande.objects.all()
#     serializer_class = CommandeSerializer


class PlantViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class SeedViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer


class StockViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class VenteViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

class AchatViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Achat.objects.all()
    serializer_class = AchatSerializer