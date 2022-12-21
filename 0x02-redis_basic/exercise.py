#!/usr/bin/env python3
"""Defining the class Cache"""
from uuid import uuid4
import redis


class Cache():

    def __init__(self):
        """Defining the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """This method take a data and returns a string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
