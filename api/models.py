from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time



class Multiplicator(models.Model):
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

	SEED_CATEGORIES = (
		('Souches', 'Souches'),
		('Pré_Bases', 'Pré_Bases'),
		('Base', 'Base'),
		('Cerifiés', 'Cerifiés'),
		)
	category = models.CharField(max_length=30,choices=SEED_CATEGORIES, verbose_name='Category')
	plant = models.ForeignKey(Plant,on_delete=models.PROTECT)
	prix = models.PositiveIntegerField()
	disponible = models.BooleanField(default=True)
	photo = models.ImageField(upload_to="media/", null=True, blank=True)
	etat_sanitaire = models.TextField(max_length=30)
	variety    = models.ForeignKey("Variety", on_delete=models.PROTECT)
	


	def __str__(self):
		return  f"{self.plant} {self.category} {self.prix} {self.disponible}"


class Stock(models.Model):
    seed = models.ForeignKey(
        Seed, default=None, on_delete=models.CASCADE)
    quantite_achetee= models.ForeignKey("Achat",on_delete=models.CASCADE)
    quantite_actuelle = models.FloatField(default=0, verbose_name='quantité actuelle')
    date = models.DateField(blank=True, default=timezone.now)


    def __str__(self):
        return f"{self.quantite_achetee.quantite_achetee} du {self.date}"


    def save(self,*args,**kwargs):
    	pass

class Vente(models.Model):
	client = models.ForeignKey(Client,on_delete=models.CASCADE)
	quantite_vendue = models.PositiveIntegerField(default=0)
	prix_de_vente = models.CharField(max_length=30)
	seed = models.ForeignKey(Seed,on_delete=models.CASCADE)
	date = models.DateField(blank=False,default=timezone.now)

	def ___str__(self):
		return f"{self.client}{self.quantite_vendue} {self.seed} le {self.date} "

class Achat(models.Model):
	seed = models.ForeignKey("Seed", on_delete=models.PROTECT)
	quantite_achetee = models.FloatField()
	date = models.DateTimeField(blank=True, default=timezone.now)
	user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
	details = models.TextField(blank=True, null=True)
	prix_achat = models.FloatField()

	def __str__(self):
		return f"{self.seed.plant} par {self.user.username}"

	def save(self, *args, **kwargs):
		if self.quantite_achetee<0:
			raise Exception("Achat.achetee cannot be negative number")
		super().save(*args, **kwargs)

	class Meta:
		ordering = ["seed"]
