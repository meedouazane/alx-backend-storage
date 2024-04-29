#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    result = logs_collection.find()
    methods = {
        'GET': 0,
        'POST': 0,
        'PUT': 0,
        'PATCH': 0,
        'DELETE': 0
    }
    i = 0
    for log in result:
        i += 1
        met = log.get('method')
        if met in methods:
            methods[met] += 1

    print(f'{i} logs')
    print('Methods:')
    for method, number in methods.items():
        print(f'    method {method}: {number}')
    status = 0
    result2 = logs_collection.find()
    for check in result2:
        if check.get('path') == '/status':
            status += 1
    print(f'{status} status check')
