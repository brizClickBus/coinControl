from django.db import models
from django.contrib.auth.models import User
from bank.models import Cards

# Create your models here.
class Category(models.Model):
    seguimentoChoice = (("ENTRADA","Entrada"),("SAIDA","Saida"))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20,choices=seguimentoChoice)
    createdAt = models.DateTimeField()
    
    class Meta:
        verbose_name = "Category" # Define o nome que será exibido no admin
        verbose_name_plural = "Categorys" # Define o nome no plural


class Transaction(models.Model):
    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    paymentMethod = models.ForeignKey(Cards, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Transaction" # Define o nome que será exibido no admin
        verbose_name_plural = "Transactions" # Define o nome no plural