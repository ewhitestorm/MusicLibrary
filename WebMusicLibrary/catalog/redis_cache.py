import redis
import json
import datetime


class UserRedis():
    def get_user_redis(value_object):
        user_redis = redis.Redis()
        attr_user = {'username': str(value_object), 'entry_time': str(datetime.datetime.now())}
        user_redis.set('user_redis',json.dumps(attr_user))
        
    def set_user_redis():
        user_redis = redis.Redis()
        return user_redis.mget('user_redis')
