## Imports

# Python standard library
import logging
import sys



# Postgres and SQL
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2

# Package
import functions


## Logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('bapdb')


## Globals
USERNAME = 'postgres'
DBNAME = 'bapdb'
PORT = '5432'
PASSWORD = 'password'
HOST = 'localhost'


def _create_database(username, password, host, port, db_name):
    """
    """
    engine = _get_engine(username, password, host, port, db_name)

    ## create a database (if it doesn't exist)
    if not database_exists(engine.url):
        create_database(engine.url)


def _get_engine(username, password, host, port, db_name):
    """
    """

    return create_engine(
        'postgres://{}:{}@{}:{}/{}' \
            .format(username, password, host, port, db_name))


def _get_server_connection(
    db_name=DBNAME, username=USERNAME, password=PASSWORD, host=HOST):
    """
    """
    # Create connection and cursor object to insert info into db
    return psycopg2.connect(database=db_name, user=username, password=password, host=host)


class SQLHandle(object):
    """
    """
    CURSORNAME = 'cur'

    @staticmethod
    def get_create(db_name=DBNAME, username=USERNAME, password=PASSWORD, host=HOST):
        """
        """
        server_connection = _get_server_connection(db_name, username, password, host)
        return SQLHandle(server_connection)

    def __init__(self, server_connection):
        """
        """
        self.con = server_connection
        self.cursor = self.con.cursor()

    def execute(self, command):
        '''
        '''
        self.cursor.execute(command)
        try:
            results = self.cursor.fetchall()
            if len(results) == 0:
                results = None
        except psycopg2.ProgrammingError:
            logger.info('Programming error in fetching results')
            results = None

        return results

if __name__ == '__main__':
    sql_handle = SQLHandle.get_create()

    command = functions.CREATE_BAP_TRANS
    print(sql_handle.execute(command))
