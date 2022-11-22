[In English](https://github.com/ewhitestorm/MusicLibrary/README_EN.md)
# MusicLibrary

Маленький проект "Музыкальная библиотека", который позволяет вносить данные о: музыкальных альбомах, исполнителях, песнях и видеть результат/статистику на web-странице на локальном сервере.

#### Реализация: 
  * [Python](https://www.python.org/)
  * [HTML](https://html.spec.whatwg.org/multipage/)

#### Собран с помощью:
  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://www.django-rest-framework.org/)
  * [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
  * [SQLite](https://www.sqlite.org/index.html)

## Установка

Клонируйте репозиторий [MusicLibrary](https://github.com/ewhitestorm/MusicLibrary.git) и выполните следующие команды в терминале.

```bash
py -3 -m venv .venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Результат

Страницы HTML:
  * http://127.0.0.1:8000/
  * http://127.0.0.1:8000/admin/
  * http://127.0.0.1:8000/Album/
  * http://127.0.0.1:8000/Singer/
  * http://127.0.0.1:8000/Song/
    
Страницы Django Rest Framework:
  * http://127.0.0.1:8000/album/
  * http://127.0.0.1:8000/album/1/ или [../album/2/](http://127.0.0.1:8000/album/2/) и так далее
  * http://127.0.0.1:8000/singer/
  * http://127.0.0.1:8000/singer/1/ или [../singer/2/](http://127.0.0.1:8000/singer/2/) и так далее
  * http://127.0.0.1:8000/song/
  * http://127.0.0.1:8000/song/1/ или [../song/2/](http://127.0.0.1:8000/song/2/) и так далее
  
Страница Swagger:
  * http://127.0.0.1:8000/swagger/
