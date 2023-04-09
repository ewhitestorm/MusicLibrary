#!/usr/bin/bash
cd WebMusicLibrary/
sudo service postgresql start
redis-server
python3 manage.py runserver 8080
