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


def get_num_baps_on_date(sql_handle, bapper, bap_type, date_dt):
    """
    """
    query = "select count(*) from {} where {} = %(bapper)s and {}::date = %(date_dt)s and {} = %(bap_type)s" \
        .format(schema.BapTransSchema.TABLE_NAME,
                schema.BapTransSchema.BAPPER,
                schema.BapTransSchema.TIMESTAMP,
                schema.BapTransSchema.BAPTYPE)
    return sql_handle.execute(query, bapper=bapper, date_dt=date_dt, bap_type=bap_type)


def _create_players(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.PlayersSchema)


def get_player(sql_handle, player_name):
    """
    """
    query = "select * from {} where {} = %(player_name)s" \
        .format(schema.PlayersSchema.TABLE_NAME,
                schema.PlayersSchema.NAME)
    player = sql_handle.execute(query, player_name=player_name)
    print("PLAYER!!!!", player)
    return player



def get_player_level(sql_handle, player_name):
    """
    """
    query = "select {} from {} where {} = %(player_name)s" \
        .format(schema.PlayersSchema.LEVEL,
                schema.PlayersSchema.TABLE_NAME,
                schema.PlayersSchema.NAME)
    return sql_handle.execute(query, player_name = player_name)


def get_max_baps_allowed(sql_handle, player):
    """
    """
    pass



def _create_levels(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.LevelsSchema)
