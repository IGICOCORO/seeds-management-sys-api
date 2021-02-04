from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

# Create your models here.
class Actor(models.Model):
	user = models.OneToOneField(User,on_delete= models.CASCADE)
	tel = models.PositiveIntegerField()


	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"


class Adress_distributor(models.Model):
	province = models.CharField(max_length=30)
	commune = models.CharField(max_length=30)
	colline = models.CharField(max_length=20)
	phone_number = models.PositiveIntegerField()
	distributor = models.OneToOneField(Actor,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.province} {self.commune} {self.colline} {self.phone_number}'


class SeedCategory(models.Model):
	SEED_CHOICES = (
		('Souches', 'Souches'),
		('Pré_Bases', 'Pré_Bases'),
		('Base', 'Base'),
		('Cerifiés', 'Cerifiés'),
		)
	nom = models.CharField(max_length=30,choices=SEED_CHOICES, verbose_name='Category')

	def __str__(self):
		return self.nom

	class Meta:
		verbose_name = 'Seed Category'
		verbose_name_plural = 'Seed Categories'
 

class RateSeed(models.Model):
 	validé = models.BooleanField(null=False)
 	actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
 	def __str__(self):
 		return f" {self.actor} {self.status}"


class Plant(models.Model):
    nom = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return f'{self.nom}'

    class Meta:
        ordering = ["nom"]

class Client(models.Model):
    nom = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=24)

    class Meta:
        unique_together = ('nom', 'tel')

    def __str__(self):
        return f"{self.nom} {self.tel}"


class Variety(models.Model):
	nom = models.CharField(max_length=30)
	caracteristique =  models.TextField()

	def __str__(self):
		return f"{ self.nom} {self.caracteristique}"


class Seed(models.Model):
	nom = models.OneToOneField(Plant,on_delete=models.PROTECT)
	rate = models.OneToOneField(RateSeed,on_delete=models.CASCADE)
	prix = models.PositiveIntegerField()
	disponible = models.BooleanField(default=True)
	exp_date = models.DateField(editable=True, null=False)
	etat_sanitaire = models.TextField(max_length=30)
	variety    = models.ForeignKey(Variety, on_delete=models.PROTECT)


	def __str__(self):
		return  f"{self.nom} {self.prix} {self.disponible} {self.quantite} {self.etat_sanitaire} {self.variety} "


class Stock(models.Model):
    plant = models.ForeignKey(
        Plant, default=None, on_delete=models.CASCADE)
    lot = models.CharField(max_length=30)
    quantite_initiale = models.FloatField(
        default=None, verbose_name='quantité initial')
    quantite_actuelle = models.FloatField(
        editable=False, default=None, verbose_name='quantité actuelle')
    date = models.DateField(blank=True, default=timezone.now)


    def __str__(self):
        return f"{self.plant} {self.quantite_actuelle} du {self.date}"

class Commande(models.Model):
    actor = models.ForeignKey(
        Actor, on_delete=models.PROTECT)
    client = models.ForeignKey(
        Client, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=timezone.now)
    
    def __str__(self):
        return f"de {self.client.nom} par {self.client.user.username}"