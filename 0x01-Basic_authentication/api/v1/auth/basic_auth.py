#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for Basic auth.
"""
import base64
import binascii
from typing import TypeVar
from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic auth API authentication manager.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract the Base64 part of the header.
        """
        if authorization_header and isinstance(authorization_header, str) and\
                authorization_header.startswith("Basic "):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode value of a Base64 string.
        """
        if base64_authorization_header and isinstance(
                base64_authorization_header, str):
            try:
                return base64.b64decode(base64_authorization_header).decode(
                        'utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Get the User instance based on his email and password.
        """
        if user_email is None or not -isinstance(user_email, str):
            return None
        if user_pwd is None or not -isinstance(user_pwd, str):
            return None
        User.load_from_file()
        users = User.search({"email": user_email})
        if len(users) == 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
