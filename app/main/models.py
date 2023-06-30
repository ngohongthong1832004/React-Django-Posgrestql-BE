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
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')



class InfoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    countLike = models.IntegerField(default=0)
    countComment = models.IntegerField(default=0)
    countWishlist = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='images/', default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class WishlistLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']

class WishlistFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=2000)
    name = models.CharField(max_length=2000)
    subName = models.CharField(default="", max_length=2000)
    releaseDate = models.CharField(max_length=2000)
    year = models.CharField(max_length=2000)
    length = models.CharField(default="90min", max_length=2000)
    like = models.IntegerField(default=0)
    IMDb = models.CharField(default="0.0", max_length=2000)
    star = models.IntegerField(default=0)
    desc = models.CharField(max_length=2000)
    casts = models.CharField(max_length=2000)
    genres = models.CharField(max_length=2000)
    countries = models.CharField(max_length=2000)
    productions = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChatBox(models.Model):
    movies = models.OneToOneField(Movie, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    totalChatItem = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']

class ChatItem(models.Model):
    chatbox = models.ForeignKey(ChatBox, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    like = models.IntegerField(default=0)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']

class ChatReply(models.Model):
    chatitem = models.ForeignKey(ChatItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    like = models.IntegerField(default=0)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
    
    