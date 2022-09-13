import email
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Anime(models.Model):
    name = models.CharField(max_length=100, unique=True)
    episode = models.PositiveSmallIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
#    image=models.ImageField(upload_to='images/', null=True, blank=True)                                     ## set images
    anime_genre = models.ForeignKey('Anime_genre', on_delete=models.CASCADE)

class Anime_genre(models.Model):
    genre = models.CharField(max_length=20, unique=True)
    
class Anime_label(models.Model):
    label = models.CharField(max_length=15, unique=True)
    anime = models.ManyToManyField('Anime')
    
class Person(models.Model):
    gender_choices= (('m', 'male'), ('f', 'female'), ('o', 'other'))                                           ### Create choice.py
    country_choices = (('mexico', 'Mexico'), ('japan', 'Japan'))
    
    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices = gender_choices, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=15, choices = country_choices, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
#    image=models.ImageField(upload_to='images/', null=True, blank=True)    
    
class Artist(Person):
    nickname = models.CharField(max_length=20, null=True, blank=True)
    anime = models.ManyToManyField('Anime', on_delete=models.CASCADE)
    

class User(Person):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=30, unique=True)
#    password                                            ###pasword login


class Activity(models.Model):
    status_choice = (('want_to_watch', 'want_to_watch'),('watching', 'watching'),('temporary_stopped', 'temporary_stopped'),('left', 'left')) 
    
    activity_status = models.CharField(max_length=15, choices= status_choice)
    episodes_watched = models.PositiveSmallIntegerField(default=0) 
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    
class Calification(models.Model):
    episodes_watched = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    ) 
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    
class Post(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    views = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.ForeignKey('Post_category', on_delete=models.CASCADE)

class Post_category(models.Model):
    category = models.CharField(max_length=20, unique=True)
    
class Post_label(models.Model):
    label = models.CharField(max_length=15, unique=True)
    post = models.ManyToManyField('Post', on_delete=models.CASCADE)

                