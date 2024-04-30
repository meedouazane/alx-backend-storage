#!/usr/bin/env python3
""" Writing strings to Redis"""
import uuid
import redis
from typing import Union, Callable


class Cache:
    """ Cache class """

    def __init__(self) -> None:
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

    def get(self, key: str, fn: Callable = None):
        """
        get method that take a key string argument
        and an optional Callable argument named fn
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return None

    def get_str(self, data):
        """
        :return: data as string
        """
        return str(data)

    def get_int(self, data):
        """
        :return: data as int
        """
        return int(data)
