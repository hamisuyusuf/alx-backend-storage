#!/usr/bin/env python3
"""
This module defines a Cache class for storing and retrieving data
using Redis as the backend.
"""

import redis
import uuid
from typing import Union


class Cache:
    """Cache class for storing data in Redis."""

    def __init__(self):
        """Initialize the Cache instance with a Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
