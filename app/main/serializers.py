from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', "is_staff", "is_superuser", "id"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        InfoUser.objects.create(user=user, id=user.id)

        return user

class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoUser
        fields = ('__all__')


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


class Movieerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("__all__") 



