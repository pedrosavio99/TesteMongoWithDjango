from django.db import models


# Create your models here.
class User(models.Model):
    matricula = models.CharField(max_length=4, unique=True)
    senha = models.CharField(max_length=4)

    def __str__(self):
        return self.matricula
