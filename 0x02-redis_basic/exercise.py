#!/usr/bin/env python3
"""Defining the class Cache"""
from uuid import uuid4
import redis
from typing import Union, Callable, Optional, Union


class Cache():

    def __init__(self):
        """Defining the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method take a data and returns a string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Optional[
            Union[str, bytes, int, float]]:
        """This function will convert the data to an expected format"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, value: bytes) -> str:
        """Converts a byte string to string"""
        return value.decode('utf-8')

    def get_int(self, value: bytes) -> int:
        """Converts a byte string to integer"""
        return int(value)
