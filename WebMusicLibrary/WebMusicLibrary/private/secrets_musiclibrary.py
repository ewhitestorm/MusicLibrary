import json
from django.core.exceptions import ImproperlyConfigured


class SecretConfig(object):
    def __init__(self, path):
        self._path = path
        self._config = None
        self._read()

    def _read(self):
        try:
            with open(self._path) as f:
                self._config = json.loads(f.read())
        except FileNotFoundError:
            raise ImproperlyConfigured(
                "Error opening file at '{}'".format(self._path)
            )

    def get(self, key, value=None):
        try:
            if value is not None:
                return self._config[key][value]
            else:
                return self._config[key]
        except KeyError:
            error_message = "Json file has not key '{0}'".format(key)
            raise ImproperlyConfigured(error_message)
            