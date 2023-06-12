from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class UserSub(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

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