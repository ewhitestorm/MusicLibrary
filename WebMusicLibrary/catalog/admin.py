from django.contrib import admin
from .models import Album, Singer, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','release_date', 'name_singer', 'author')
    list_filter = ('title', 'release_date', 'name_singer', 'author')

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('name_singer', 'author')
    list_filter = ('name_singer', 'author')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name_song', 'name_singer', 'title', 'number', 'author')
    list_filter = ('name_singer', 'title', 'author')
