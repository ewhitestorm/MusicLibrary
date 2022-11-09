from django.contrib import admin
from .models import Album, Singer, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','release_date')
    list_filter = ('title', 'release_date')

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_filter = ('name_singer', 'song')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name_song', 'show_singer', 'number')
    list_filter = ('singer', 'album')

