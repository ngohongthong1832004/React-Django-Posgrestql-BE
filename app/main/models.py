from django.db import models
from django.contrib.auth.models import User



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



class InfoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    countLike = models.IntegerField(default=0)
    countComment = models.IntegerField(default=0)
    countWishlist = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='images/', default='null')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return self.firstName + " " + self.lastName
    
    def __str__(self):
        return self.user.username



class Movie(models.Model):
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