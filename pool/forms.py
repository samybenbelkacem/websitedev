from django.forms import ModelForm
from pool.models import Movie, Cinema, Showing


class MovieForm(ModelForm):
     class Meta:
         model = Movie
         fields = ['title', 'year', 'overview', 'trailer_url', 'language', 'poster']


class CinemaForm(ModelForm):
     class Meta:
         model = Cinema
         fields = ['user', 'name', 'adress', 'zip_code', 'nbr_rooms', 'siren']


class ShowingForm(ModelForm):
     class Meta:
         model = Showing
         fields = ['cinema', 'movie', 'schedule']
