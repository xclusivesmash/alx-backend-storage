#!/usr/bin/env python3
"""
module: exercise
description: creates a Cache class.
"""
import redis
import uuid
from typing import Union


class Cache:
    """class definition.
    Attributes:
        _redis (redis-data-type): redis data type.
    Methods:
        __init__(self):
        store(slef, data):
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string.
        Args:
            data (any): data to be stored.
        Returns:
            string variable.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
