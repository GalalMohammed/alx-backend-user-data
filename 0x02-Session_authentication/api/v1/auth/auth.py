#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to manage the API authentication.
"""
import os
from typing import List, TypeVar
from flask import request


class Auth():
    """API authentication manager.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Define which routes don't need authentication.
        """
        if path and path[-1] != '/':
            path += '/'
        if not (path and excluded_paths and path in excluded_paths):
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ Request validation.
        """
        if request and request.headers.get("Authorization"):
            return request.headers["Authorization"]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method.
        """
        return None

    def session_cookie(self, request=None) -> object:
        """Get a cookie value from a request.
        """
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
