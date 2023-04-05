[In English](https://github.com/ewhitestorm/MusicLibrary/blob/main/README_EN.md)
# MusicLibrary

Проект "Музыкальная библиотека" - это блокнот для коллекционирования: музыкальных альбомов, исполнителей, текстов песен.

#### Реализация: 
  * [Python](https://www.python.org/)
  * [HTML](https://html.spec.whatwg.org/multipage/)

#### Собран с помощью:
  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://www.django-rest-framework.org/)
  * [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
  * [PostgreSQL](https://www.postgresql.org/)
  * [SQLite](https://www.sqlite.org/)
  * [Docker](https://hub.docker.com/)
  * [SQLAlchemy](https://www.sqlalchemy.org/)
  * [Redis](https://redis.io/)

#### Тестирование:
  * [Pytest](https://docs.pytest.org/)

#### Адаптирован для:
  * Windows 
  * Linux Debian ([WSL](https://learn.microsoft.com/ru-ru/windows/wsl/about/))

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
После чего откройте браузер и перейдите по ссылке из блока "Результат".

## Установка с помощью docker-compose (только для версии [1.0](https://github.com/ewhitestorm/MusicLibrary/tree/Version_1.0))

Зарегистрируйтесь на сайте [Docker](https://hub.docker.com/)
Загрузите образ (последнюю версию), в терминале прописав команду:
```bash
docker pull ewstorm/musiclibrary:latest
```
Запустите образ, в терминале прописав команду:
```bash
docker run -p 8000:8001 --name musiclibrary-django ewstorm/musiclibrary
```
Откройте браузер и перейдите по ссылке из блока "Результат".

## Результат

Страница HTML:
  * http://127.0.0.1:8000/
