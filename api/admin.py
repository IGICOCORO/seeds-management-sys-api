from django.contrib import admin
from .models import *

# @admin.register(Actor)
# class ActorAdmin(admin.ModelAdmin):
# 	list_display = "user", "tel"
# 	list_filter = "user", "tel"
# 	search_field = "user", "tel"
# 	ordering = "user", "tel"

# 	select_related = True

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "nom", "tel"
	list_filter = "nom", "tel"
	search_field = "nom", "tel"
	ordering = "nom", "tel"

@admin.register(AdressDistributor)
class AdressDistributorAdmin(admin.ModelAdmin):
	list_display = "province", "commune","colline","phone_number"
	list_filter = "province", "commune","colline","phone_number"
	search_field = "province", "commune","colline","phone_number"
	ordering = "province", "commune"

	select_related = True

@admin.register(Plant)

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
	list_display = "plant", 
	list_filter = "plant", 
	search_field = "plant", 
	ordering = "plant", 

	select_related = True

# @admin.register(Commande)
# class CommandeAdmin(admin.ModelAdmin):
# 	list_display = "actor", "client", "date"
# 	list_filter = "actor", "client", "date"
# 	search_field = "actor", "client", "date"
# 	ordering = "actor", "client", "date"
# 	select_related = True

@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
	list_display = "nom", "caracteristique"
	list_filter = "nom", "caracteristique"
	search_field = "nom", "caracteristique"
	ordering = "nom", "caracteristique"

	select_related = True

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
	list_display = "seed","quantite_initiale","quantite_actuelle","date"
	list_filter = "seed","quantite_initiale","quantite_actuelle","date"
	search_field = "seed","quantite_initiale","quantite_actuelle","date"
	ordering = "seed","quantite_initiale","quantite_actuelle","date"

	select_related = True

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
	list_display = "seed","prix_de_vente","quantite_achetee","client"
	list_filter = "seed","prix_de_vente","client"
	search_field = "seed","prix_de_vente","client"
	ordering = "seed"

	select_related = True
