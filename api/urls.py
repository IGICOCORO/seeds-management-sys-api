from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


router = routers.DefaultRouter()

# router.register("acteur", ActorViewset)
router.register("client", ClientViewset)
router.register("Adresse_fournisseur", AdressDistributorViewset)
router.register("variete", VarietyViewset)
# router.register("commande", CommandeViewset)
router.register("user",UserViewset)
router.register("plantes", PlantViewset)
router.register("semences", SeedViewset)
router.register("stock", StockViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]