

def log_bap(sql_handle, bap):
    """
    """

    command = "insert into bap_trans(timestamp, bapper, bappee, baptype) " \
              "VALUES(%(timestamp)s, %(bapper)s, %(bappee)s, %(baptype)s)"
    return sql_handle.execute(
        command, timestamp = bap.timestamp, bapper = bap.bapper, bappee = bap.bappee, baptype = bap.type)


def create_bap_trans(sql_handle):
    """
    """
    CREATE_BAP_TRANS = \
        'CREATE TABLE IF NOT EXISTS bap_trans (timestamp TIMESTAMPTZ, bapper TEXT, bappee TEXT, baptype TEXT)'
    return sql_handle.execute(CREATE_BAP_TRANS)
