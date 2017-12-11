from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2100)])
    overview = models.TextField(max_length=3000)
    trailer_url = models.URLField("Link to the trailer", max_length=200)
    language = models.CharField(max_length=60)
    poster = models.ImageField(blank=True) #TODO
    active = models.BooleanField(default=True)


class Cinema(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    adress = models.CharField(max_length=60)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    nbr_rooms = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    siren = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])
    active = models.BooleanField(default=True)


class Showing(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    active = models.BooleanField(default=True)


class VoteMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class VoteShowing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    showing = models.ForeignKey('Showing', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class Sales(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    showing = models.ForeignKey('Showing', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
