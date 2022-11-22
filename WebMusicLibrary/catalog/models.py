from django.db import models


class Singer(models.Model):
    name_singer = models.CharField(max_length=200, 
                                   help_text='Enter artist name', 
                                   verbose_name='Artist name'
                                  )
    def __str__(self) -> str:
        return self.name_singer

class Album(models.Model):
    title = models.CharField(max_length=200, 
                            help_text='Enter album name', 
                            verbose_name='Album title'
                            )
    release_date = models.IntegerField(help_text='Enter album release year', 
                                       verbose_name='Album release year'
                                      )
    def __str__(self) -> str:
        return self.title

class Song(models.Model):
    name_song = models.CharField(max_length=200, 
                                 help_text='Enter song title', 
                                 verbose_name='Name of the song'
                                )
    singer = models.ManyToManyField('Singer', 
                                    help_text='Select artist name', 
                                    verbose_name='Artist name'
                                   )
    album = models.ManyToManyField('Album',
                                   help_text='Choose an album name', 
                                   verbose_name='Album title'
                                  )
    number = models.IntegerField(help_text='Enter the number of the song in the album', 
                                 verbose_name='Album song number'
                                 )
    def show_singer(self):
        return ', '.join([singer.name_singer for singer in self.singer.all()])
    show_singer.short_description = 'Artist name'
    
    def __str__(self) -> str:
        return self.name_song
