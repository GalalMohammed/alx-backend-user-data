#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for Basic auth.
"""
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
