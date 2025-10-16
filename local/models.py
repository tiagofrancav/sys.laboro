from django.db import models

# Create your models here.
class localidade (models.Model):
    nome = models.CharField(max_length=80)
    logradouro = models.CharField(max_length=150)
    bairro = models.CharField(max_length=80)
    numero = models.PositiveBigIntegerField(max_length=80)

