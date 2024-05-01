#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import redis
from functools import wraps
import requests
from typing import Callable


def tracker(fn: Callable) -> Callable:
    """ Decorator for get_page """
    @wraps(fn)
    def wrapper(url: str) -> str:
        client = redis.Redis()
        client.incr(f'count:{url}')
        cache_page = client.get(f'{url}')
        if cache_page:
            return cache_page.decode('utf-8')
        request = fn(url)
        client.set(f'{url}', request, 10)
        return request
    return wrapper


@tracker
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and returns it.
    """
    req = requests.get(url)
    return req.text
