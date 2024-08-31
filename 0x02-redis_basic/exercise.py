#!/usr/bin/env python3
"""
This module defines a Cache class for storing and retrieving data
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of
      inputs and outputs for a method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create the keys for inputs and outputs in Redis
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the input arguments in the inputs list
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    # Retrieve the list of inputs and outputs from Redis
    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)

    # Print the replay summary
    print(f"{method_name} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        inp_str = inp.decode('utf-8')
        out_str = out.decode('utf-8')
        print(f"{method_name}(*{inp_str}) -> {out_str}")


class Cache:
    """Cache class for storing and retrieving data in Redis."""

    def __init__(self):
        """Initialize the Cache instance with a Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally
          apply a conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve data from Redis as a string.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve data from Redis as an integer.
        """
        return self.get(key, fn=int)
