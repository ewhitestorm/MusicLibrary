[На русском](https://github.com/ewhitestorm/MusicLibrary/blob/main/README.md)
# MusicLibrary

The project "Music Library", which allows you to enter data about: music albums, artists, songs and see the result/statistics on a web page.

#### Implementation: 
  * [Python](https://www.python.org/)
  * [HTML](https://html.spec.whatwg.org/multipage/)

#### Assembled:
  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://www.django-rest-framework.org/)
  * [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
  * [SQLite](https://www.sqlite.org/index.html)
  * [Docker](https://hub.docker.com/)

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
Then open the browser and follow the link from the "Result" block.

## Installation with docker-compose (only for version 1.0)

Register on the site [Docker](https://hub.docker.com/)
Download the image (latest version) by typing the following command in a terminal:
```bash
docker pull ewstorm/musiclibrary:latest
```
Run the image by typing the following command in a terminal:
```bash
docker run -p 8000:8001 --name musiclibrary-django ewstorm/musiclibrary
```
Then open the browser and follow the link from the "Result" block.

## Result

Page HTML:
  * http://127.0.0.1:8000/
