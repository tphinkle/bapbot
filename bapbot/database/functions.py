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

def get_baps(sql_handle, bapper=None, bappee = None, bap_type=None, date_dt=None):
    """
    """
    kwargs = {}
    conds = []
    if bapper is not None:
        kwargs['bapper'] = bapper
        conds.append('{} = %(bapper)s'.format(schema.BapTransSchema.BAPPER))
    if bappee is not None:
        kwargs['bappee'] = bappee
        conds.append('{} = %(bappee)s'.format(schema.BapTransSchema.BAPPEE))
    if bap_type is not None:
        kwargs['bap_type'] = bap_type
        conds.append('{} = %(bap_type)s'.format(schema.BapTransSchema.BAPTYPE))
    if date_dt is not None:
        kwargs['date_dt'] = date_dt
        conds.append('{}::date = %(date_dt)s'.format(schema.BapTransSchema.TIMESTAMP))

    if len(conds) > 0:
        formatted_conds = ' AND '.join(conds)
        query = "select * from {} where {}".format(schema.BapTransSchema.TABLE_NAME, formatted_conds)
    else:
        query = "select * from {}".format(schema.BapTransSchema.TABLE_NAME)


    baps = sql_handle.execute(query, **kwargs)
    if baps is None:
        return []
    return baps

def get_bapper_num_baps_on_date(sql_handle, bapper, bap_type, date_dt):
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
    players = get_player(sql_handle, player_name)
    if len(players) > 0:
        raise ValueError("Requested new player registration, but user already exists ({})".format(player_name))

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

    if players is None:
        return []

    return players[0]


def _create_levels(sql_handle):
    """
    """
    return _create_table_from_schema_object(sql_handle, schema.LevelsSchema)


def get_level(sql_handle, level):
    """
    """
    query = "select * from {} where {} = %(level)s" \
        .format(schema.LevelsSchema.TABLE_NAME,
                schema.LevelsSchema.LEVEL)
    levels = sql_handle.execute(query, level=level)

    if levels is None:
        return []

    return levels[0]
