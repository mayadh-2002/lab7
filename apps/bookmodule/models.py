from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=50, default='')
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)



