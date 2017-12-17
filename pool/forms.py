from django.forms import ModelForm
from pool.models import Movie, Cinema, Showing, VoteMovie


class MovieForm(ModelForm):
     class Meta:
        model = Movie
        fields = '__all__'


class CinemaForm(ModelForm):
     class Meta:
        model = Cinema
        fields = '__all__'


class ShowingForm(ModelForm):
     class Meta:
        model = Showing
        fields = '__all__'


class VoteMovieForm(ModelForm):
    class Meta:
        model = VoteMovie
        fields = ['movie']
