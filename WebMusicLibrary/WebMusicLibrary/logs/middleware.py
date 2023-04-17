import time
import json


#Request processing time calculation
def simple_middleware(get_response):

    def middleware(request):
        time_start = time.monotonic()
        response = get_response(request)

        data = {
            'path': request.path,
            'request_time': round(time.monotonic() - time_start, 3),
        }

        with open('WebMusicLibrary/logs/request_time.log', 'a') as f:
            f.write(json.dumps(data) + '\n')

        return response

    return middleware
