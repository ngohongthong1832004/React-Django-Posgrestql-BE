import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()

import json
from main.models import Film
from app.wsgi import *

with open('./main/model/movie-full-option.json', 'r', encoding="utf-8") as f:
    films = json.load(f)
    index = 0
    for film in films:
        temp = Film(
            id = index,
            name = film['name'],
            img = film['img'],
            year = film['year'],
            length = film['length'],
            imdb = film['imdb'],
            href = film['href'],
            desc = film['desc'],
            genres = film['genres'],
            casts = film['casts'],
            countries = film['countries'],
            production = film['production']
        )
        index += 1
        temp.save()
        # print("done !!")

from main.models import Movies
with open('./main/model/movie-full-option.json', 'r', encoding="utf-8") as f:
    films = json.load(f)
    index = 1
    for film in films:
        temp = Movies(
            id = index,
            name = film['name'],
            img = film['img'],
            year = film['year'],
            length = film['length'],
            imdb = film['imdb'],
            href = film['href'],
            desc = film['desc'],
            genres = film['genres'],
            casts = film['casts'],
            countries = film['countries'],
            production = film['production']
        )
        index += 1
        temp.save()



# from main.models import UserSub

# s = UserSub(id=3, name='admin7', age=18)
# s.save()
# s = UserSub(id=2, name='user', age=18)
# s.save()