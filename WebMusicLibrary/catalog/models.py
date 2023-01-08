from django.db import models
from django.contrib.auth.models import User


class Singer(models.Model):
    name_singer = models.CharField(max_length=200, 
                                   help_text='Enter artist name', 
                                   verbose_name='Artist name'
                                  )
    author = models.ForeignKey(User, 
                               verbose_name='Author', 
                               blank=True, null=True, 
                               on_delete=models.CASCADE
                               )

    def __str__(self) -> str:
        return self.name_singer

class Album(models.Model):
    title = models.CharField(max_length=200, 
                            help_text='Enter album name', 
                            verbose_name='Album title',
                            blank=True, null=True
                            )
    name_singer = models.CharField(max_length=200, 
                                   help_text='Enter artist name', 
                                   verbose_name='Artist name'
                                  )
    release_date = models.IntegerField(help_text='Enter album release year', 
                                       verbose_name='Album release year',
                                       blank=True, null=True
                                      )
    author = models.ForeignKey(User, 
                               verbose_name='Author', 
                               blank=True, null=True, 
                               on_delete=models.CASCADE
                               )

    def __str__(self) -> str:
        return self.title

class Song(models.Model):
    name_song = models.CharField(max_length=200, 
                                 help_text='Enter song title', 
                                 verbose_name='Name of the song'
                                )
    name_singer = models.CharField(max_length=200, 
                                   help_text='Enter artist name',
                                   verbose_name='Artist name'
                                   )
    title = models.CharField(max_length=200,
                             help_text='Enter album name',
                             verbose_name='Album title',
                             blank=True, null=True
                             )
    number = models.IntegerField(help_text='Enter the number of the song in the album', 
                                 verbose_name='Album song number',
                                 blank=True, null=True
                                 )
    author = models.ForeignKey(User, 
                               verbose_name='Author', 
                               blank=True, null=True, 
                               on_delete=models.CASCADE
                               )

    def show_singer(self):
       return ', '.join([singer.name_singer for singer in self.singer.all()])
    show_singer.short_description = 'Artist name'

    def show_album(self):
       return ', '.join([album.title for album in self.album.all()])
    show_album.short_description = 'Album title'
    
    def __str__(self) -> str:
        return self.name_song
