from rest_framework import serializers
from .models import Film, UserSub



class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = (
            "id",
            "name",
            "img",
            "year",
            "length",
            "imdb",
            "href",
            "desc",
            "genres",
            "casts",
            "countries",
            "production",
        )




