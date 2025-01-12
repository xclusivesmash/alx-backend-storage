#!/usr/bin/env python3
"""
module: exercise
description: creates a Cache class.
"""
import redis
import uuid


class Cache:
    """class definition.
    Attributes:
        _redis (redis-data-type): redis data type.
    Methods:
        __init__(self):
        store(slef, data):
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: str | bytes | int | float):
        """returns a string.
        Args:
            data (any): data to be stored.
        Returns:
            string variable.
        """
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)
