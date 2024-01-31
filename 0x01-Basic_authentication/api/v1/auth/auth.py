#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to manage the API authentication.
"""
from flask import request
from typing import List


class Auth():
    """API authentication manager.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ # TODO
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ public method.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method.
        """
        return None
