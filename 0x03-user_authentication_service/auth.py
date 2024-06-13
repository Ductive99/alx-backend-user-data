#!/usr/bin/env python3
"""Authentication Module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a hashed version of the given password
    """
    data = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(data, salt)
    return hashed_password
