#!/usr/bin/env python3
"""
Cache module using Redis.

Author: Your Name
"""

import uuid
from typing import Union
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method of the Cache class is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Generate the key using the qualified name of the method
        key = f"{method.__qualname__}_calls"

        # Increment the count for the key in Redis
        self._redis.incr(key)

        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    """
    Cache class using Redis.

    This class provides a simple interface for storing data in Redis with
    randomly generated keys.

    Author: PhenomenalAI
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance.

        It creates a Redis client and flushes the database.

        Returns:
            None
        """
        # Create a Redis client
        self._redis = redis.Redis()

        # Flush the database
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used for storing the data.
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())

        # Store the data in Redis using the generated key
        self._redis.set(key, data)

        # Return the generated key
        return key


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used for storing the data.
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())

        # Store the data in Redis using the generated key
        self._redis.set(key, data)

        # Return the generated key
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Convert data back to desired format
        """
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode("utf-8")
