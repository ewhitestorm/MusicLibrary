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

#### Тестирование:
  * [Pytest](https://docs.pytest.org/)

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

## Установка с помощью docker-compose (только для версии 1.0)

Зарегистрируйтесь на сайте [Docker](https://hub.docker.com/)
Загрузите образ (последнюю версию), в терминале прописав команду:
```bash
docker pull ewstorm/musiclibrary:latest
```
Запустите образ, в терминале прописав команду:
```bash
docker run -p 8000:8001 --name musiclibrary-django ewstorm/musiclibrary
```
После чего откройте браузер и перейдите по ссылке из блока "Результат".

## Результат

Страница HTML:
  * http://127.0.0.1:8000/
