from django.db import models
from django.contrib.auth.models import User

class Terms(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accepted = models.BooleanField()
    class Meta:
        verbose_name = "Terms" # Define o nome que será exibido no admin
        verbose_name_plural = "Terms" # Define o nome no plural    