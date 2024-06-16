#!/usr/bin/env python3
"""
Basic Authentication Module
That defines the BasicAuth class
"""
from auth import Auth


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
