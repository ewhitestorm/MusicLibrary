[In English](https://github.com/ewhitestorm/MusicLibrary/blob/main/README_EN.md)
# MusicLibrary

Проект "Музыкальная библиотека", который позволяет вносить данные о: музыкальных альбомах, исполнителях, песнях и видеть результат/статистику на web-странице.

#### Реализация: 
  * [Python](https://www.python.org/)
  * [HTML](https://html.spec.whatwg.org/multipage/)

#### Собран с помощью:
  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://www.django-rest-framework.org/)
  * [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
  * [SQLite](https://www.sqlite.org/index.html)
  * [Docker](https://hub.docker.com/)

## Установка

Клонируйте репозиторий [MusicLibrary](https://github.com/ewhitestorm/MusicLibrary.git) и выполните следующие команды в терминале:

```bash
py -3 -m venv .venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
После чего откройте браузер и перейдите по ссылкам из блока "Результат".

## Установка с помощью docker-compose

Зарегистрируйтесь на сайте [Docker](https://hub.docker.com/)
Загрузите образ (последнюю версию), в терминале прописав команду:
```bash
docker pull ewstorm/musiclibrary:latest
```
Запустите образ, в терминале прописав команду:
```bash
docker run -p 8000:8001 --name musiclibrary-django ewstorm/musiclibrary
```
После чего откройте браузер и перейдите по ссылкам из блока "Результат".

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
