## Imports

# Project
from .. import utils
from . import schema

## Globals
def _create_table_from_schema_object(sql_handle, schema_object):
    """
    """
    cols = []
    for col_name, col in schema_object.columns.items():
        cols.append(' '.join([col_name, col['type']]))
    formatted_cols = ', '.join(cols)

    CREATE_TABLE_CMD = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(schema_object.TABLE_NAME, formatted_cols)
    print(CREATE_TABLE_CMD)
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


def register_new_player(sql_handle, name, join_date, level, experience):
    """
    """
    query = "INSERT INTO {} ({}, {}, {}, {}) VALUES (%(name)s, %(join_date)s, %(level)s, %(experience)s)" \
        .format(schema.PlayersSchema.TABLE_NAME,
                schema.PlayersSchema.NAME,
                schema.PlayersSchema.JOIN_DATE,
                schema.PlayersSchema.LEVEL,
                schema.PlayersSchema.EXPERIENCE)
    result = sql_handle.execute(query, name=name, join_date=join_date, level=level, experience=experience)


def get_player(sql_handle, player_name):
    """
    """
    query = "select * from {} where {} = %(player_name)s" \
        .format(schema.PlayersSchema.TABLE_NAME,
                schema.PlayersSchema.NAME)
    players = sql_handle.execute(query, player_name=player_name)
    player_name = player[0][0]
    join_date = player[0][1]
    level = player[0][2]
    experience = player[0][3]
    player_name, join_date, level, experience



def get_player_level(sql_handle, player_name):
    """
    """
    query = "select {} from {} where {} = %(player_name)s" \
        .format(schema.PlayersSchema.LEVEL,
                schema.PlayersSchema.TABLE_NAME,
                schema.PlayersSchema.NAME)
    return sql_handle.execute(query, player_name = player_name)[2]


def get_max_baps_allowed(sql_handle, player):
    """
    """
    pass



def _create_levels(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.LevelsSchema)
