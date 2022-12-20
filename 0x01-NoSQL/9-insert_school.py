#!/usr/bin/env python3
"""Defining the insert_school method"""


def insert_school(mongo_collection, **kwargs):
    """This function inserts a new document in a collection based on kwargs"""
    instance = mongo_collection.insert_one(kwargs)
    return instance.inserted_id
