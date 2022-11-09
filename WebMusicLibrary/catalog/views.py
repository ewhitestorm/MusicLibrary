from django.shortcuts import render
from .models import Album, Singer, Song
from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers
from django.views import generic



def index(request):
    num_user = User.objects.all().count()
    num_album = Album.objects.all().count()
    num_song = Song.objects.all().count()
    num_singer = Singer.objects.all().count()

    contex = {
        'num_user': num_user,
        'num_album': num_album,
        'num_song': num_song,
        'num_singer': num_singer,
    }
    return render(request, 'index.html', contex)


class AlbumListView(generic.ListView): 
    model = Album

class SingerListView(generic.ListView): 
    model = Singer

class SongListView(generic.ListView): 
    model = Song


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class AlbumDetail(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class SingerList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = serializers.SingerSerializer

class SingerDetail(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = serializers.SingerSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer

class SongDetail(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
