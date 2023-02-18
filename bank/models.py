from django.db import models
from django.contrib.auth.models import User


class CentralBank(models.Model):
    ispb = models.IntegerField()
    name = models.CharField(max_length=250)
    code = models.FloatField()
    fullName = models.CharField(max_length=250)
    lastUpdate = models.DateTimeField()
    
    class Meta:
        verbose_name = "CentralBank" # Define o nome que será exibido no admin
        verbose_name_plural = "CentralBank" # Define o nome no plural


class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(CentralBank, on_delete=models.CASCADE)
    bankname = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    createdAt = models.DateTimeField()
    class Meta:
        verbose_name = "Bacnk" # Define o nome que será exibido no admin
        verbose_name_plural = "Banks" # Define o nome no plural


class Cards(models.Model):
    creditoChoices = (('SIM','Sim'),('NAO','Não'),('OS DOIS','Os dois'))
   
    banks = models.ForeignKey(Bank, on_delete=models.CASCADE)
    titularname = models.CharField(max_length=225)
    type = models.CharField(max_length=20,choices=creditoChoices)
    lastNumber = models.IntegerField()
    expiryYear = models.IntegerField()
    expiryMonth = models.IntegerField()
    surname = models.CharField(max_length=225)
    createdAt = models.DateTimeField()

    class Meta:
        verbose_name = "Card" # Define o nome que será exibido no admin
        verbose_name_plural = "Cards" # Define o nome no plural


class Meal(models.Model):
    typeChoice = (('VR','VR'),('VA','VA'),('CRÉDITO','Crédito'),('OUTROS','Outros'))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compane = models.CharField(max_length=225)
    type = models.CharField(max_length=20,choices=typeChoice)
    createdAt = models.DateTimeField()
    
    class Meta:
        verbose_name = "Meal" # Define o nome que será exibido no admin
        verbose_name_plural = "Meals" # Define o nome no plural