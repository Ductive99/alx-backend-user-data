#!/usr/bin/env python3
"""Authentication Module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

from typing import Union


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes Auth class
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """Registers a new user with a hashed password
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError("User {} already exists".format(email))


def _hash_password(password: str) -> bytes:
    """Returns a hashed version of the given password
    """
    data = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(data, salt)
    return hashed_password
