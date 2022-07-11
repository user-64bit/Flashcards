from django.db import models

# Create your models here.

class Data(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100000)
    tag = models.CharField(max_length=20)
    choice = models.IntegerField()
    
    def __str__(self):
        return self.title
