## Imports

# Postgres and SQL
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2

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


def _get_server_connection(db_name, username, password, host):
    """
    """
    # Create connection and cursor object to insert info into db
    return SQLHandle(psycopg2.connect(database = db_name, user = username, password = password, host = host))


class SQLHandle(object):
    """
    """

    @staticmethod
    def get_create(db_name=DBNAME, username=USERNAME, password=PASSWORD, host=HOST):
        """
        """
        connection = _get_server_connection(db_name, username, password, host)
        return SQLHandle(connection)

    def __init__(self, server_connection):
        """
        """
        self.con = server_connection
        self.cursor = self.con.cursor()

    def query(self, command):
        '''
        '''
        self.cursor.execute(command)
        results = SQLHandle.cursor.fetchall()

        if len(results) == 0:
            results = None

        return results
