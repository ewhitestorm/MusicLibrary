#!/usr/bin/bash
cd WebMusicLibrary/
sudo service postgresql start
redis-cli ping 2> ./logging/redislog.txt
result=`tac ./logging/redislog.txt | grep -m 1 .`
if [[ "$result" == "Could not connect"* ]]
then
/usr/local/bin/redis-server --daemonize yes
else
redis-server
fi
: > ./logging/redislog.txt
python3 manage.py runserver 8080
