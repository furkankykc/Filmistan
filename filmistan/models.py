import os

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Year(models.Model):
    yy = models.IntegerField()

    def __str__(self):
        return str(self.yy)


class Actor(models.Model):
    name = models.CharField(max_length=20, default='')
    surname = models.CharField(max_length=20, default='')
    birthDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Trailer(models.Model):
    code = models.TextField(default='')

    def __str__(self):
        return self.code


class Director(models.Model):
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    birthDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


def get_image_path_2(self, filename):
    return os.path.join(BASE_DIR, str('static/photos/kullanıcılar'), str(User.username + '.jpg'))


def get_image_path(self, filename):
    return os.path.join(BASE_DIR, str('static/photos/filmler'), str(slugify(self.title) + '.jpg'))


class Film(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='film')
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    cast = models.ManyToManyField(Actor)
    rating = models.FloatField(default='0')
    createDate = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, default='Film Özeti')
    list_display = ('title', 'year'),
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    youtube_trailer = models.ManyToManyField(Trailer)

    @property
    def desc(self):
        desc = self.description.replace('[', '').replace('\'', '').replace(']', '')
        self.description = desc
        self.save()
        return desc

    def __str__(self):
        return self.title

    def release(self):
        self.createDate = timezone.now()
        self.save()
