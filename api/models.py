from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

# Create your models here.
# class Actor(models.Model):
# 	user = models.OneToOneField(User,on_delete= models.CASCADE)
# 	tel = models.PositiveIntegerField()


# 	def __str__(self):
# 		return f"{self.user.username} {self.tel}"


class AdressDistributor(models.Model):
	province = models.CharField(max_length=30)
	commune = models.CharField(max_length=30)
	colline = models.CharField(max_length=20)
	phone_number = models.PositiveIntegerField()
	distributor = models.OneToOneField(User,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.distributor.username} {self.commune} {self.province} {self.phone_number}'


class Plant(models.Model):
    plant = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return f'{self.plant}'

    class Meta:
        ordering = ["plant"]

class Client(models.Model):
    nom = models.CharField(max_length=30)
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

	SEED_CHOICES = (
		('Souches', 'Souches'),
		('Pré_Bases', 'Pré_Bases'),
		('Base', 'Base'),
		('Cerifiés', 'Cerifiés'),
		)
	category = models.CharField(max_length=30,choices=SEED_CHOICES, verbose_name='Category')
	plant = models.ForeignKey(Plant,on_delete=models.PROTECT)
	prix = models.PositiveIntegerField()
	disponible = models.BooleanField(default=True)
	photo = models.ImageField(upload_to="media/", null=True, blank=True)
	etat_sanitaire = models.TextField(max_length=30)
	variety    = models.ForeignKey("Variety", on_delete=models.PROTECT)


	def __str__(self):
		return  f"{self.nom} {self.category} {self.prix} {self.disponible}"


class Stock(models.Model):
    seed = models.ForeignKey(
        Seed, default=None, on_delete=models.CASCADE)
    quantite_initiale = models.FloatField(
        default=None, verbose_name='quantité initial')
    quantite_actuelle = models.FloatField(
        editable=False, default=0, verbose_name='quantité actuelle')
    date = models.DateField(blank=True, default=timezone.now)


    def __str__(self):
        return f"{self.quantite_actuelle} du {self.date}"

# class Commande(models.Model):
#     actor = models.ForeignKey(
#         Actor, on_delete=models.PROTECT)
#     client = models.ForeignKey(
#         Client, blank=True, null=True, on_delete=models.CASCADE)
#     date = models.DateField(blank=True, default=timezone.now)
    
#     def __str__(self):
#         return f"de {self.client.nom} par {self.client.user.username}"