from django.db import models


# Create your models here.
class User(models.Model):
    matricula = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=60)
    senha = models.CharField(max_length=4)

    def __str__(self):
        return self.matricula
