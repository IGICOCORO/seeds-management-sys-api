from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "nom", "tel"
	list_filter = "nom", "tel"
	search_field = "nom", "tel"
	ordering = "nom", "tel"

@admin.register(Multiplicator)
class MultiplicatorAdmin(admin.ModelAdmin):
	list_display = "province", "commune","colline","phone_number"
	list_filter = "province", "commune","colline","phone_number"
	search_field = "province", "commune","colline","phone_number"
	ordering = "province", "commune"

	select_related = True

@admin.register(Plant)

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
	list_display = "plant","disponible" 
	list_filter = "plant","disponible" 
	search_field = "plant","disponible" 
	ordering = "plant", 

	select_related = True


@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
	list_display = "nom", "caracteristique"
	list_filter = "nom", "caracteristique"
	search_field = "nom", "caracteristique"
	ordering = "nom", "caracteristique"

	select_related = True

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
	list_display = "achat","quantite","resultat","date"
	list_filter = "achat","quantite","resultat","date"
	search_field = "achat","quantite","resultat","date"
	ordering = "achat","quantite","resultat","date"

	select_related = True

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
	list_display = "stock","quantite_vendue","client","prix_de_vente"
	list_filter = "stock","quantite_vendue","client","prix_de_vente"
	search_field = "stock","quantite_vendue","client","prix_de_vente"
	ordering = "stock",

	select_related = True


@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
	list_display = "seed","quantite_achetee","date","user","details","prix_achat"
	list_filter = "seed","quantite_achetee","date","prix_achat","details"
	search_field = "seed","quantite_achetee","user","prix_achat","details"
	ordering = "seed",
	select_related = True

