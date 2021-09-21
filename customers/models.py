from django.db import models

class Customers(models.Model):
    company = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    information = models.CharField(max_length=500)