#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines filter_datum function.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Get the log message obfuscated.
    """
    for field in fields:
        message = re.sub(field + r'=[^' + separator + ']+',
                         field + ':' + redaction, message)
    return message
