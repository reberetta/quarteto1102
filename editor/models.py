from django.db import models


class Editor(models.Model):
    name = models.CharField(max_length=100)
    legal_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)
    address_loc = models.CharField(max_length=100)
    address_number = models.IntegerField()
    address_cep = models.CharField(max_length=9)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=2)
