#!/usr/bin/env python3
""" Tasks 0 to 4 """

import re
from typing import List
import logging
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated """
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
        return message


class RedactingFormatter(logging.Formatter):
    """ Update the class to accept a list of strings fields constructor argument.
    Implement the format method to filter values in incoming log records
    using filter_datum. Values for fields in fields should be filtered. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor Method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
   """ function that takes no arguments and returns a logging.Logger object """
   log = logging.getLogger('user_data')
   log.setLevel(logging.INFO)
   log.propagate = False

   sh = logging.StreamHandler()
   formatter = RedactingFormatter(PII_FIELDS)
   sh.setFormatter(formatter)
   log.addHandler(sh)

   return log

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connector to the database 
    (mysql.connector.connection.MySQLConnection object) """
    connection_db = mysql.connector.connection.MySQLConnection(
            user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
            password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
            host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=getenv('PERSONAL_DATA_DB_NAME'))

    return connection_db


def main():
    """ Implement a main function that takes no arguments and returns nothing """
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    log = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        log.info(str_row.strip())

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
