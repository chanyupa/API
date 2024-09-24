from django.db import models

# Create your models here.
class Mypj(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)