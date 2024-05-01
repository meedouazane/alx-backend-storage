#!/usr/bin/env python3
""" Writing strings to Redis"""
import uuid
import redis
from typing import Union, Callable


class Cache:
    """ Cache class """

    def __init__(self):
        """ init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        store an instance of the Redis
        client as a private variable
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
