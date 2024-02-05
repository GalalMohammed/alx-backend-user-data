#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for Session auth.
"""
import uuid
from models.user import User
from .auth import Auth


class SessionAuth(Auth):
    """Session auth API authentication manager.
    """

    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get a User ID based on a Session ID.
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> object:
        """Get a User instance based on a cookie value.
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Delete the user session (logout).
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del SessionAuth.user_id_by_session_id[session_id]
        return True
