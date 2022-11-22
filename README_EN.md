[На русском](https://github.com/ewhitestorm/MusicLibrary/blob/main/README.md)
# MusicLibrary

A small project "Music Library", which allows you to enter data about: music albums, artists, songs and see the result/statistics on a web page on a local server.

#### Implementation: 
  * [Python](https://www.python.org/)
  * [HTML](https://html.spec.whatwg.org/multipage/)

#### Assembled:
  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://www.django-rest-framework.org/)
  * [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
  * [SQLite](https://www.sqlite.org/index.html)

## Installation

Clone the repository [MusicLibrary](https://github.com/ewhitestorm/MusicLibrary.git) and run the following commands in a terminal.

```bash
py -3 -m venv .venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Result

Pages HTML:
  * http://127.0.0.1:8000/
  * http://127.0.0.1:8000/admin/
  * http://127.0.0.1:8000/Album/
  * http://127.0.0.1:8000/Singer/
  * http://127.0.0.1:8000/Song/
    
Pages Django Rest Framework:
  * http://127.0.0.1:8000/album/
  * http://127.0.0.1:8000/album/1/ or [../album/2/](http://127.0.0.1:8000/album/2/) etc.
  * http://127.0.0.1:8000/singer/
  * http://127.0.0.1:8000/singer/1/ or [../singer/2/](http://127.0.0.1:8000/singer/2/) etc.
  * http://127.0.0.1:8000/song/
  * http://127.0.0.1:8000/song/1/ or [../song/2/](http://127.0.0.1:8000/song/2/) etc.
  
Pages Swagger:
  * http://127.0.0.1:8000/swagger/
