#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines filtered_logger.
"""

import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get a connector to the database.
    """
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(user=db_username, password=db_password,
                                   host=db_host, database=db_name)
