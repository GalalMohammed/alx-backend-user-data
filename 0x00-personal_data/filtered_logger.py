#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines filter_datum function.
"""

import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """Get the log message obfuscated.
    """
    for field in fields:
        message = re.sub(field + r'=[^' + separator + ']+',
                         field + ':' + redaction, message)
    return message
