from django.db import models


class Singer(models.Model):
    name_singer = models.CharField(max_length=200, 
                                   help_text='Введите имя исполнителя', 
                                   verbose_name='Имя исполнителя'
                                  )
    def __str__(self) -> str:
        return self.name_singer

class Album(models.Model):
    title = models.CharField(max_length=200, 
                            help_text='Введите назание альбома', 
                            verbose_name='Название альбома'
                            )
    release_date = models.IntegerField(help_text='Введите год выпуска альбома', 
                                       verbose_name='Год выпуска альбома'
                                      )
    def __str__(self) -> str:
        return self.title

class Song(models.Model):
    name_song = models.CharField(max_length=200, 
                                 help_text='Введите название песни', 
                                 verbose_name='Название песни'
                                )
    singer = models.ManyToManyField('Singer', 
                                    help_text='Выберите имя исполнителя', 
                                    verbose_name='Имя исполнителя'
                                   )
    album = models.ManyToManyField('Album',
                                   help_text='Выберите название альбома', 
                                   verbose_name='Название альбома'
                                  )
    number = models.IntegerField(help_text='Введите номер песни в альбоме', 
                                 verbose_name='Номер песни в альбоме'
                                 )
    def show_singer(self):
        return ', '.join([singer.name_singer for singer in self.singer.all()])
    show_singer.short_description = 'Имя исполнителя'
    
    def __str__(self) -> str:
        return self.name_song
