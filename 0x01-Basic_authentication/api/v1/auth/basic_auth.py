#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for Basic auth.
"""
import base64
import binascii
from .auth import Auth


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
