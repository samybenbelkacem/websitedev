"""moncine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from login import views as login_views
from pool import views as pool_views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^vote/movie/$', pool_views.vote_movie_form, name='vote_movie'),
    url(r'^add/(?P<table_name>\w+)/$', pool_views.populate_db, name='populate-db'),
    url(r'^movies/$', pool_views.MovieListView.as_view(), name='movie-list'),
    url(r'^signup/$', login_views.signup, name='signup'),
    url(r'^movie_details/$', pool_views.MovieDetailView, name='movie_details'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
