from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

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
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', validated_data.get('email', '_@').split('@')[0])
        )
        
        InfoUser.objects.create(user=user, id=user.id)

        return user

class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoUser
        fields = ('__all__')




class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("__all__") 

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        chat_box = ChatBox.objects.create(movies=movie, totalChatItem=0)
        return movie

class WishlistLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistLike
        fields = ("__all__")
    def create(self, validated_data):
        return super().create(validated_data)

class WishlistFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistFollow
        fields = ("__all__")
    def create(self, validated_data):
        return super().create(validated_data)


class ChatBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBox
        fields = ("__all__")
    def create(self, validated_data):
        return super().create(validated_data)

class ChatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatItem
        fields = ("__all__")
    def create(self, validated_data):
        return super().create(validated_data)

class ChatReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatReply
        fields = ("__all__")
    def create(self, validated_data):
        return super().create(validated_data)

        



