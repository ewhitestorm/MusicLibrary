<i><p align="right">[English](https://github.com/ewhitestorm/MusicLibrary/blob/Version_3.0/README_EN.md)</p></i>
###### [Version_3.0](https://github.com/ewhitestorm/MusicLibrary.git) - Linux версия.
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
$ sudo apt-get update
$ sudo apt-get install python3-venv
$ python3.9 -m venv .venv
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
```
В VSCode подключитесь к WSL и в bash-терминале выполните команду для запуска bash сценария:
```bash
$ source musiclibrary.sh
или
$ . musiclibrary.sh
```
После чего откройте браузер и перейдите по ссылке из блока "Результат".

## Установка с помощью docker-compose (только для версии [1.0](https://github.com/ewhitestorm/MusicLibrary/tree/Version_1.0))

Зарегистрируйтесь на сайте [Docker](https://hub.docker.com/)
Загрузите образ (последнюю версию), прописав команду в терминале:
```bash
docker pull ewstorm/musiclibrary:latest
```
Запустите образ, с помощью команды:
```bash
docker run -p 8000:8001 --name musiclibrary-django ewstorm/musiclibrary
```
Откройте браузер и перейдите по ссылке из блока "Результат".

## Результат

Страница HTML:
  * http://127.0.0.1:8080/
