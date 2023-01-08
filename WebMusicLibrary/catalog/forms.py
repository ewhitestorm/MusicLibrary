from django.forms import ModelForm
from .views import *
from .models import Album, Singer, Song


class CreateSingerForm(ModelForm):
    class Meta:
        model = Singer
        fields = ['name_singer']

class CreateSongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ['title', 'name_singer']
        fields = ['name_song', 'number']

class CreateAlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ['name_singer']
        fields = ['title', 'release_date']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']
    