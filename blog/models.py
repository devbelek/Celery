from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/')


class Checks(models.Model):
    img = models.ImageField(upload_to='checks/')
