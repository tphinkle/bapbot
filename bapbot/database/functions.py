## Imports

# Postgres and SQL
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2

## Globals
username = 'prestonh'
dbname = 'bapbot'

def _create_database():
    """
    """
    engine = create_engine('postgres://%s@localhost/%s'%(username,dbname))
    #print(engine.url)

    ## create a database (if it doesn't exist)
    if not database_exists(engine.url):
        create_database(engine.url)
    pass
