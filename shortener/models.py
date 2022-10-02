from django.db import models

# Create your models here.
class Url(models.Model):
    bLink = models.CharField(max_length=1000)
    shLink = models.CharField(max_length=20)


