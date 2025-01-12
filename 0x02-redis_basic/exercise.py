#!/usr/bin/env python3
"""
module: exercise
description: creates a Cache class.
"""
import redis
import uuid
from typing import Any, Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count method calls from cache class.
    Args:
        method (Callable): callable object.
    Returns:
        Callable.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Calls a given method after incrementing its call.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    """Tracks the call details of a method.
    Args:
        method (Callable): callable object.
    Returns:
        callable.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Returns the method's output.
        """
        input_key = '{}:inputs'.format(method.__qualname__)
        output_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    """Displays the call history of a Cache class' method.
    Args:
        fn (Callable): callback function.
    Returns:
        nothing.
    """
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    input_key = '{}:inputs'.format(fxn_name)
    output_key = '{}:outputs'.format(fxn_name)
    fxn_call_count = 0
    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))
    print('{} was called {} times:'.format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(input_key, 0, -1)
    fxn_outputs = redis_store.lrange(output_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fxn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))


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

    @call_history
    @count_calls
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
