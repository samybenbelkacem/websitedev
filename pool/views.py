# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from pool.models import Movie, Cinema, Showing
from pool.forms import MovieForm, CinemaForm, ShowingForm


def populate_db(request, table_name):
    if table_name=='movie':
        generic_form = MovieForm
    if table_name=='cinema':
        generic_form = CinemaForm
    if table_name=='showing':
        generic_form = ShowingForm
    if request.method == 'POST':
        form = generic_form(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': "New " + table_name + " was added successfully"}
            return redirect('home')
    else:
        form = generic_form()
    return render(request, 'populate.html', {'form': form})


class MovieListView(ListView):

    model = Movie
