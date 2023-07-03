# Generated by Django 4.2.2 on 2023-07-03 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('totalChatItem', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ChatItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chatbox')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ChatReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chatitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('img', models.CharField(max_length=2000)),
                ('year', models.CharField(max_length=2000)),
                ('length', models.CharField(max_length=2000)),
                ('imdb', models.CharField(max_length=2000)),
                ('href', models.CharField(max_length=2000)),
                ('desc', models.CharField(max_length=2000)),
                ('genres', models.CharField(max_length=2000)),
                ('casts', models.CharField(max_length=2000)),
                ('countries', models.CharField(max_length=2000)),
                ('production', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
                ('subName', models.CharField(default='', max_length=2000)),
                ('releaseDate', models.CharField(max_length=2000)),
                ('year', models.CharField(max_length=2000)),
                ('length', models.CharField(default='90min', max_length=2000)),
                ('like', models.IntegerField(default=0)),
                ('IMDb', models.CharField(default='0.0', max_length=2000)),
                ('star', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=2000)),
                ('casts', models.CharField(max_length=2000)),
                ('genres', models.CharField(max_length=2000)),
                ('countries', models.CharField(max_length=2000)),
                ('productions', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='WishlistFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='LikeChatReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatreply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chatreply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='LikeChatItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chatitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('countLike', models.IntegerField(default=0)),
                ('countComment', models.IntegerField(default=0)),
                ('countWishlist', models.IntegerField(default=0)),
                ('avatar', models.ImageField(default='null', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DisLikeChatReply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatreply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chatreply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='DisLikeChatItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chatitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='chatbox',
            name='movies',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
    ]
