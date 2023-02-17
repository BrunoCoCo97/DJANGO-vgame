from django.db import models

class Vgames(models.Model):
    nombre = models.CharField(max_length=50)
    