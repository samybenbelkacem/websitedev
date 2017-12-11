from django.contrib import admin

# Register your models here.

from pool.models import Movie, Cinema, Showing

class MovieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Movie, MovieAdmin)

class CinemaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cinema, CinemaAdmin)

class ShowingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Showing, ShowingAdmin)
