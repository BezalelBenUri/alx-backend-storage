#!/usr/bin/env python3
"""
Cache module using Redis.

Author: Your Name
"""

import uuid
from typing import Union
import redis


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[bytes, None]:
        """
        Retrieve data from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the data.
            fn (Optional[Callable]): Optional callable to convert the data back to the desired format.

        Returns:
            Union[bytes, None]: The retrieved data in bytes or None if the key does not exist.
        """
        # Retrieve the data from Redis
        data = self._redis.get(key)

        # Apply the conversion function if provided
        if fn is not None and data is not None:
            data = fn(data)

        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve string data from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the data.

        Returns:
            Union[str, None]: The retrieved string data or None if the key does not exist.
        """
        return self._redis.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve integer data from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the data.

        Returns:
            Union[int, None]: The retrieved integer data or None if the key does not exist.
        """
        return self.get(key, fn=int)
