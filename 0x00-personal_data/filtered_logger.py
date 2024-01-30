#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines filter_datum function.
"""

import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Get the log message obfuscated.
    """
    for field in fields:
        message = re.sub(field + r'=[^' + separator + ']+',
                         field + '=' + redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init method.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values.
        """
        record.msg = filter_datum(self.fields, RedactingFormatter.REDACTION,
                                  record.getMessage(),
                                  RedactingFormatter.SEPARATOR)
        return super().format(record)
