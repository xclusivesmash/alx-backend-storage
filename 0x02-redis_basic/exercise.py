#!/usr/bin/env python3
"""
module: exercise
description: creates a Cache class.
"""
import redis
import uuid
from typing import Union, Callable


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
        self._redis.flushdb(True)

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

    def get(self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """gets data from a redis object"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """gets a string object."""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """gets an integer object."""
        return self.get(key, lambda x: int(x))
