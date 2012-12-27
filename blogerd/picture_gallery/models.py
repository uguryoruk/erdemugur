from django.db import models

class Picture(models.Model):
    pass


class Gallery(models.Model):
    name = models.CharField(max_length=30)
    pictures = models.ManyToManyField(Picture)

