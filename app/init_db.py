import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
import django
django.setup()

import json
from app.wsgi import *


from main.models import Movie
from main.models import ChatBox
import random


import json

with open("./main/dummy_data/dummy_data.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    for movie in movies:
        movie_instance = Movie.objects.create(
            img=movie["img"] if "img" in movie else "null",
            name=movie["name"] if "name" in movie else "null",
            subName=movie["subName"] if "subName" in movie else "null",
            releaseDate=movie["release"] if "release" in movie else "null",
            year=movie["year"] if "year" in movie else "null",
            length=movie["length"] if "length" in movie else "null",
            like=movie["like"] if "like" in movie else random.randint(0, 1000),
            IMDb=movie["imdb"] if "imdb" in movie else round(random.uniform(0.0, 9.0),1),
            star=movie["star"] if "star" in movie else random.randint(0, 5),
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


superuser = User.objects.create_superuser(username="admin", email="admin@gmail.com", password="admin", first_name = "admin", last_name = "☻")
infoAdmin = InfoUser(
    user = superuser,
    id = 1,
    countLike = 0,
    countComment = 0,
    countWishlist = 0,
)
infoAdmin.save()
print("Superuser created successfully.")

usersTable =  [
    {"name": "Olivia Johnson", "email": "olivia.johnson@example.com", "password" : "123456"},
    {"name": "Ethan Smith", "email": "ethan.smith@example.com", "password" : "123456"},
    {"name": "Ava Davis", "email": "ava.davis@example.com", "password" : "123456"},
    {"name": "Noah Brown", "email": "noah.brown@example.com", "password" : "123456"},
    {"name": "Isabella Miller", "email": "isabella.miller@example.com", "password" : "123456"},
    {"name": "Lucas Wilson", "email": "lucas.wilson@example.com", "password" : "123456"},
    {"name": "Mia Taylor", "email": "mia.taylor@example.com", "password" : "123456"},
    {"name": "Liam Anderson", "email": "liam.anderson@example.com", "password" : "123456"},
    {"name": "Sophia Martinez", "email": "sophia.martinez@example.com", "password" : "123456"},
    {"name": "Jackson Clark", "email": "jackson.clark@example.com", "password" : "123456"},
    {"name": "Emma Thompson", "email": "emma.thompson@example.com", "password" : "123456"},
    {"name": "Aiden Lee", "email": "aiden.lee@example.com", "password" : "123456"},
    {"name": "Harper Harris", "email": "harper.harris@example.com", "password" : "123456"},
    {"name": "Benjamin Robinson", "email": "benjamin.robinson@example.com", "password" : "123456"},
    {"name": "Amelia Turner", "email": "amelia.turner@example.com", "password" : "123456"},
    {"name": "Henry Walker", "email": "henry.walker@example.com", "password" : "123456"},
    {"name": "Charlotte Hill", "email": "charlotte.hill@example.com", "password" : "123456"},
    {"name": "Michael Mitchell", "email": "michael.mitchell@example.com", "password" : "123456"},
    {"name": "Ava Young", "email": "ava.young@example.com", "password" : "123456"},
    {"name": "James Nelson", "email": "james.nelson@example.com", "password" : "123456"},
]

for user in usersTable:
    user = User.objects.create_user( username =user["email"], password = user["password"], email = user["email"], first_name = user["name"].split(" ")[0], last_name = user["name"].split(" ")[1])
    infoUser = InfoUser(
        user = user,
        id = user.id,
        countLike = 0,
        countComment = 0,
        countWishlist = 0,
    )
    infoUser.save()
print("Users created successfully.")
