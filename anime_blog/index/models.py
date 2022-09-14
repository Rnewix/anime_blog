from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Person(models.Model):
    #model base for Artist and user
    GENDERCHOICES= (
        ('m', _('male')), 
        ('f', _('female')), 
        ('o', _('other'))
        )                                                                                           ### Create choice.py
    COUNTRYCHOICES = (
        (1, _('Mexico')), 
        (2, _('Japan')),
        (3, _('United States')),
        (4, _('other'))
        )
    
    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices = GENDERCHOICES, blank=True)
    birthday = models.DateField(null=True, blank=True)
    country = models.PositiveSmallIntegerField(choices = COUNTRYCHOICES, null=True, blank=True)
    description = models.TextField(blank=True)
    image=models.ImageField(upload_to='images/', null=True, blank=True)                                  
    
    
class Artist(Person):
    nickname = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
      return self.last_name + ' ' + self.first_name


class User(Person):                                                                                     ##auth_User??
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=30, unique=True)
#    password                                                                                            ###pasword login

    def __str__(self):
        return self.username
                
                
class Anime_genre(models.Model):
    genre = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.genre
    
class Anime_label(models.Model):
    label = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.label
    
class Anime(models.Model):
    name = models.CharField(max_length=100, unique=True)
    episode = models.PositiveSmallIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    image=models.ImageField(upload_to='images/', null=True, blank=True)                                   
    genre = models.ForeignKey(Anime_genre, on_delete=models.PROTECT, null=True, blank=True)
    label = models.ManyToManyField(Anime_label, through='Anime_Animelabel', blank=True)
    artist = models.ManyToManyField(Artist, through='Anime_Artist', blank=True)
    
    def __str__(self):
        return self.name
    

class Anime_Animelabel(models.Model):
    #Join table-model for relation Anime - Anime_label
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    anime_label = models.ForeignKey(Anime_label, on_delete=models.CASCADE)
    

class Anime_Artist(models.Model):
    #Join table-model for relation Anime - Artist
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Activity(models.Model):
    CHOICES = (
        (1, _('want to watch')), 
        (2, _('watching')),
        (3, _('temporary stopped')),
        (4, _('left'))
        )
    
    activity_status = models.PositiveSmallIntegerField(choices= CHOICES)
    episodes_watched = models.PositiveSmallIntegerField(default=0, blank=True) 
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + '' + self.activity_status + '' + self.anime
    
    
class Calification(models.Model):
    calification = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    ) 
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.anime + ' calification:' + self.calification
    

class Post_label(models.Model):
    label = models.CharField(max_length=15, unique=True)
    
    
class Post_category(models.Model):
    category = models.CharField(max_length=20, unique=True)    
    
    
class Post(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    views = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default= 1)                                    ###### Corregir usuario default
    category = models.ForeignKey(Post_category, on_delete=models.SET_NULL, null=True, blank=True)
    label = models.ManyToManyField(Post_label, through='Post_Postlabel', blank=True)
    
    def __str__(self):
        return self.user + ' comment ' + self.date + '' + self.id

class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default= "anonymous")
    
    def __str__(self):
        return self.user + ' comment ' + self.date + '' + self.id

    
class Post_Postlabel(models.Model):
    #Join table-model for relation Post - Post_label
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_label = models.ForeignKey(Post_label, on_delete=models.CASCADE)
                
       
       
       
