#!/usr/bin/env python3
"""
This module defines a Cache class for storing and retrieving data
using Redis as the backend with data conversion capabilities.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class for storing and retrieving data in Redis."""

    def __init__(self):
        """Initialize the Cache instance with a Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally apply a conversion function.

        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): A function to apply to the data before returning it.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve data from Redis as a string.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Union[str, None]: The retrieved data
            as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve data from Redis as an integer.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Union[int, None]: The retrieved data
             as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
