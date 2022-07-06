#!/usr/bin/env python3
""" Task 1 """

import re
from typing import List
import logging
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ that returns the log message obfuscated """
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message


if __name__ == '__main__':
    main()
