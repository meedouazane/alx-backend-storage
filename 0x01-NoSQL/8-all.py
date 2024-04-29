#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """ lists all documents in a collection """
    if mongo_collection is None:
        return "[]"
    all_lst = mongo_collection.find()
    return all_lst
