#!/usr/bin/env python3
"""Session Authentication Module
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authentication Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session_id for a user_id
        """
        if type(user_id) == str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a session ID
        """
        if type(session_id) == str:
            return self.user_id_by_session_id.get(session_id)
