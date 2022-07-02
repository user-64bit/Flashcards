from django.db import models

# Create your models here.

class Data(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=1000)
    tag = models.CharField(max_length=20)
