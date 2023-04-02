import sqlalchemy
import redis
import json
import re
from sqlalchemy.orm import Session
from .redis_cache import UserRedis
from .models_sqlalchemy import User


class EngineSqlAlchemy():
    engine = sqlalchemy.create_engine('sqlite:///sqlite3.db')
    engine.connect()


def get_data():
    with Session(EngineSqlAlchemy.engine) as session:
        list_attr = session.query(User.id,User.username,User.date).all()
        print(list_attr)


def set_data():
    list_attr = (re.findall('"([^"]*)"', str(UserRedis.set_user_redis())))
    with Session(EngineSqlAlchemy.engine) as session:
        list_elems = User(username=list_attr[1], date=list_attr[3])
        try:
            session.add(list_elems)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            session.close()


def del_data():
    with Session(EngineSqlAlchemy.engine) as session:
        session.query(User).filter(User.date == None).delete(synchronize_session=False)
        session.commit()
        session.close()
