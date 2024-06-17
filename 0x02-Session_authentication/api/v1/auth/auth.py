#!/usr/bin/env python3
"""Module that manages the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires auth
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Make paths always end with '/'
        for ep in excluded_paths:
            if ep.startswith(path) or path.startswith(ep):
                return False
            elif ep[-1] == "*":
                if path.startswith(ep[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Auth header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User
        """
        return None
