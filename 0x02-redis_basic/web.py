#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import redis
from functools import wraps
import requests
from typing import Callable


def tracker(fn: Callable) -> Callable:
    """Decorator for get_page"""

    @wraps(fn)
    def wrapper(url: str) -> str:
        client = redis.Redis()
        client.incr(f'count:{url}')
        cache_page = client.get(f'{url}')
        if cache_page:
            return cache_page.decode('utf-8')
        try:
            request = fn(url)
        except Exception as e:
            return f"Error: {e}"
        client.set(f'{url}', request, ex=10)
        return request

    return wrapper


@tracker
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a particular URL and return it.

    :param url: The URL of the page.
    :return: The HTML content of the page.
    """
    try:
        req = requests.get(url)
        req.raise_for_status()
        return req.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch URL: {e}")


# Example usage:
if __name__ == "__main__":
    print(get_page("http://slowwly.robertomurray.co.uk"))
