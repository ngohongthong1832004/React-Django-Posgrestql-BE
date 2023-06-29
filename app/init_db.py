import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
import django
django.setup()

import json
from app.wsgi import *


from main.models import Movie
from main.models import ChatBox


import json

with open("./main/model/movie-full-option.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    for movie in movies:
        movie_instance = Movie.objects.create(
            img=movie["img"] if "img" in movie else "null",
            name=movie["name"] if "name" in movie else "null",
            subName=movie["subName"] if "subName" in movie else "null",
            releaseDate=movie["release"] if "release" in movie else "null",
            year=movie["year"] if "year" in movie else "null",
            length=movie["length"] if "length" in movie else "null",
            like=movie["like"] if "like" in movie else 0,
            IMDb=movie["imdb"] if "imdb" in movie else 0,
            star=movie["star"] if "star" in movie else 0,
            desc=movie["desc"] if "desc" in movie else "null",
            casts=", ".join(movie["casts"]) if "casts" in movie else "null",
            genres=", ".join(movie["genres"]) if "genres" in movie else "null",
            countries=", ".join(movie["countries"]) if "countries" in movie else "null",
            productions=", ".join(movie["production"]) if "production" in movie else "null"
        )
        ChatBox.objects.create(movies=movie_instance, id=movie_instance.id, totalChatItem=0)





from main.models import User
from main.models import InfoUser
from django.contrib.auth import get_user_model

User = get_user_model()

# Create the superuser
superuser = User.objects.create_superuser(username="admin", email="admin@gmail.com", password="admin")

infoAdmin = InfoUser(
    user = superuser,
    id = 1,
    countLike = 66,
    countComment = 88,
    countWishlist = 99,
)
infoAdmin.save() 

print("Superuser created successfully.")
