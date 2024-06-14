#!/usr/bin/env python3
"""Authentication Module
"""
import bcrypt
import uuid
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

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with a hashed password
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if the password is valid for the given email
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Sets a UUID for the session_id of the given email
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        new_id = _generate_uuid()
        self._db.update_user(user.id, session_id=new_id)
        return new_id


def _hash_password(password: str) -> bytes:
    """Returns a hashed version of the given password
    """
    data = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(data, salt)
    return hashed_password


def _generate_uuid() -> str:
    """Generates a string representation of a new UUID
    """
    return str(uuid.uuid4())
