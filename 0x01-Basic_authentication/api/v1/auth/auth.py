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
        s_path = path if path.endswith('/') else path + '/'
        s_ep = [p if p.endswith('/') else p + '/' for p in excluded_paths]

        if s_path in s_ep:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User
        """
        return None
