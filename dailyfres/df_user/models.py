from django.db import models

# Create your models here.

class Entry(models.Model):
    """"""
    user = models.CharField(max_length=20)
    upassword = models.CharField(max_length=10)
    postbox = models.CharField(max_length=20)
