#!/usr/bin/env python3
""" Writing strings to Redis"""
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method Callable
    argument and returns a Callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(fn: Callable) -> None:
    """
    display the history of calls of a particular function
    """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [item.decode('utf-8')
              for item in client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [item.decode('utf-8')
               for item in client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was called {calls} times:')
    for inp, outp in zip(inputs, outputs):
        print(f'{fn.__qualname__}(*{inp}) -> {outp}')


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """ init method"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)
        self.call_count = 0

    @count_calls
    @call_history
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        store an instance of the Redis
        client as a private variable
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> (
            Union)[str, int, float, bytes]:
        """
        get method that take a key string argument
        and an optional Callable argument named fn
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn:
            return fn(data)
        else:
            return data

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
