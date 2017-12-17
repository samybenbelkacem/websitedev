# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from pool.models import Movie, Cinema, Showing
from pool.forms import MovieForm, CinemaForm, ShowingForm, VoteMovieForm

def populate_db(request, table_name):
    if table_name=='movie':
        generic_form = MovieForm
    if table_name=='cinema':
        generic_form = CinemaForm
    if table_name=='showing':
        generic_form = ShowingForm
    if table_name=='vote':
        generic_form = VoteMovieForm
    if request.method == 'POST':
        form = generic_form(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            context = {'message': "New " + table_name + " was added successfully"}
            return redirect('home')
    else:
        form = generic_form()
    return render(request, 'populate.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MovieListView(ListView):
    model = Movie

class MovieDetailView(DetailView):
    model = Movie

    context_object_name = 'movie_details'   # your own name for the list as a template variable

# def vote_movie_form(request):
#     if request.method == 'POST':
#         form = VoteMovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # vote = form.save(commit=False)
#             # vote.user = request.user
#             # vote.save()
#             return redirect('home')
#     else:
#         form = VoteMovieForm()
#     return render(request, 'populate.html', {'form': form})
