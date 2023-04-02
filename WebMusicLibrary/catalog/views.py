import redis
from django.shortcuts import render, redirect
from .models import Album, Singer, Song
from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CreateSingerForm, CreateSongForm, CreateAlbumForm
from django.http import Http404
from .redis_cache import UserRedis
from .sqlalchemy_db import get_data, set_data, del_data


def home(request):
    try:
        context = {}
        return render(request, 'home.html', context)
    except:
        raise Http404()

@login_required

def index(request):
    temp_elem = []
    Song_list = []
    Albums_list = []
    cut_song_list = []

    num_user = User.objects.all().count()
    
    UserRedis.get_user_redis(str(request.user))
    
    def temp(self):
        for elem in self.objects.filter(author=request.user):
            temp_elem.append(str(elem))
        return (temp_elem)
    
    num_singer = len(list(set(temp(Singer))))
    num_song = len(Song.objects.filter(author=request.user))
    num_album = len(Album.objects.filter(author=request.user))

    if request.method == 'POST':
        singer_form = CreateSingerForm(request.POST)
        song_form = CreateSongForm(request.POST)
        album_form = CreateAlbumForm(request.POST)
        
        if singer_form.is_valid() or song_form.is_valid() or album_form.is_valid():
            def in_field(elem):
                if elem == str():
                    return '0'
                else:
                    return elem

            count_singer = list(set(temp(Singer))).count(str(singer_form['name_singer'].value()))
            
            if count_singer < 1:
                Singer.objects.create(name_singer = singer_form['name_singer'].value(), 
                                      author = request.user
                                      )
            
            for song_elem in Song.objects.filter(author=request.user): 
                list_song = []
                list_song.extend([song_elem.name_song, song_elem.name_singer, song_elem.title, song_elem.number])
                Song_list.append(list_song)
            
            new_list_song = [in_field(song_form['name_song'].value()),
                             in_field(singer_form['name_singer'].value()),
                             in_field(album_form['title'].value()),
                             int(in_field(song_form['number'].value()))
                             ]

            for x in Song_list:
                cut_song_list.append(x[0:2])

            if new_list_song[0:2] not in cut_song_list:
                Song.objects.create(name_song = in_field(song_form['name_song'].value()),
                                    name_singer = in_field(singer_form['name_singer'].value()),
                                    title = in_field(album_form['title'].value()),
                                    number = int(in_field(song_form['number'].value())),
                                    author = request.user
                                    )

            for album_elem in Album.objects.filter(author=request.user): 
                list_album = [] 
                list_album.extend([album_elem.title, album_elem.name_singer, album_elem.release_date])
                Albums_list.append(list_album)
                            
            new_list_album = [in_field(album_form['title'].value()),
                             in_field(singer_form['name_singer'].value()),
                             int(in_field(album_form['release_date'].value()))
                             ]
            
            if new_list_album not in Albums_list and in_field(album_form['title'].value()) != '0' and in_field(album_form['release_date'].value()) != '0':
                Album.objects.create(title = in_field(album_form['title'].value()),
                                     name_singer = in_field(singer_form['name_singer'].value()),
                                     release_date = int(in_field(album_form['release_date'].value())),
                                     author = request.user
                                     )
            
            return redirect('index')
    else:
        singer_form = CreateSingerForm()
        song_form = CreateSongForm()
        album_form = CreateAlbumForm()
    
    set_data()
    get_data()
    # del_data()
    
    context = {
        'num_user': num_user,
        'num_album': num_album,
        'num_song': num_song,
        'num_singer': num_singer,
        'singer_form': singer_form,
        'song_form': song_form,
        'album_form': album_form,
    }
    return render(request, 'index.html', context)


class AlbumListView(generic.ListView): 
    model = Album
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('title')

class SingerListView(generic.ListView):
    model = Singer
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('name_singer')

class SongListView(generic.ListView): 
    model = Song
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('name_song')

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class AlbumDetail(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class SingerList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = serializers.SingerSerializer

class SingerDetail(generics.RetrieveAPIView):
    queryset = Singer.objects.all()
    serializer_class = serializers.SingerSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer

class SongDetail(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
