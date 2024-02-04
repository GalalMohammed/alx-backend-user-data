#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for Session auth.
"""
import uuid
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
