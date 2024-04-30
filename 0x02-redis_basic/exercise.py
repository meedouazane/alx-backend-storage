#!/usr/bin/env python3
""" Writing strings to Redis"""
import uuid
import redis
from typing import Union


class Cache:
    """ Cache class """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
