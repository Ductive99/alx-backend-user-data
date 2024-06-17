#!/usr/bin/env python3
"""
Basic Authentication Module
That defines the BasicAuth class
"""
from .auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth Class that inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header
        """
        if type(authorization_header) == str:
            if authorization_header[:6] == "Basic ":
                return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Returns decoded value of authorization header
        """
        if type(base64_authorization_header) == str:
            try:
                result = base64.b64decode(
                    base64_authorization_header,
                    validate=True
                )
                return result.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        Returns the user's email and password from the decoded base64
        authorization header seperated by a colon
        """
        if type(decoded_base64_authorization_header) == str:
            if ":" not in decoded_base64_authorization_header:
                return (None, None)
            else:
                data = decoded_base64_authorization_header.split(":", 1)
                return (data[0], data[1])
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """
        Returns the corresponding User instance based on the
        given email and password
        """
        if type(user_email) == type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
                if users[0].is_valid_password(user_pwd):
                    return users[0]
            except Exception:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves user's data
        """
        auth_header = self.authorization_header(request)
        b64_token = self.extract_base64_authorization_header(auth_header)
        token = self.decode_base64_authorization_header(b64_token)
        email, password = self.extract_user_credentials(token)
        return self.user_object_from_credentials(email, password)
