## Imports

# Project
from .. import utils
from . import schema

## Globals

def _create_table_from_schema_object(sql_handle, schema_object):
    """
    """
    cols = []
    for key, item in schema_object.columns.items():
        cols.append(' '.join([key, item]))
    formatted_cols = ','.join(cols)

    CREATE_TABLE_CMD = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(schema_object.table_name, formatted_cols)
    return sql_handle.execute(CREATE_TABLE_CMD)


def _create_bap_trans(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.BapTransSchema)

def log_bap(sql_handle, bap):
    """
    """

    command = "insert into {}(timestamp, bapper, bappee, baptype) VALUES(%(timestamp)s, %(bapper)s, %(bappee)s, %(baptype)s)"
    return sql_handle.execute(
        command, timestamp = bap.timestamp, bapper = bap.bapper, bappee = bap.bappee, baptype = bap.type)


def get_num_baps_on_date(sql_handle, date_dt):
    """
    """
    query = "select * from {} where bapper = %(bapper)s and now()::date = %(date_dt)s".format(BAP_TRANS)
    return sql_handle.execute(query, bapper=bapper, date=date_dt)


def _create_players(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.PlayersSchema)


def get_player_level(sql_handle, bapper):
    """
    """
    queery = "select {} from {} where {} = %(bapper)s" \
        .format(schema.PlayersSchema.LEVEL,
                schema.PlayersSchema.TABLE_NAME,
                schema.PlayersSchema.NAME)


def _create_levels(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.LevelsSchema)
