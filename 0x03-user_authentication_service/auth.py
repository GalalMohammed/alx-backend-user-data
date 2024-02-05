#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines _hash_password function.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash the input password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
