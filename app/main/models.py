from django.db import models


class Film(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=2000)
    img = models.CharField(max_length=2000)
    year = models.CharField(max_length=2000)
    length = models.CharField(max_length=2000)
    imdb = models.CharField(max_length=2000)
    href = models.CharField(max_length=2000)
    desc = models.CharField(max_length=2000)
    genres = models.CharField(max_length=2000)
    casts = models.CharField(max_length=2000)
    countries = models.CharField(max_length=2000)
    production = models.CharField(max_length=2000)

   

class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=2000)
    img = models.CharField(max_length=2000)
    year = models.CharField(max_length=2000)
    length = models.CharField(max_length=2000)
    imdb = models.CharField(max_length=2000)
    href = models.CharField(max_length=2000)
    desc = models.CharField(max_length=2000)
    genres = models.CharField(max_length=2000)
    casts = models.CharField(max_length=2000)
    countries = models.CharField(max_length=2000)
    production = models.CharField(max_length=2000)