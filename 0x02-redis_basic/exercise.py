#!/usr/bin/env python3
""" Writing strings to Redis"""
import uuid
import redis
from typing import Union


class Cache:
    """ Cache class """

    def __init__(self):
        """ init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]):
        """
        store an instance of the Redis
        client as a private variable
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn):
        """
        get method that take a key string argument
        and an optional Callable argument named fn
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return None

    def get_str(self, key):
        """
        :param key: string id
        :return: data as string
        """
        data = self._redis.get(key)
        return str(data)

    def get_int(self, key):
        """
        :param key: string id
        :return: data as int
        """
        data = self._redis.get(key)
        return int(data)
