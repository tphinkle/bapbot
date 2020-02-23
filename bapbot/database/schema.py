## Imports

# Python standard library
from collections import OrderedDict


TEXT_TYPE = 'TEXT'
TIMESTAMPTZ_TYPE = 'TIMESTAMPTZ'
UNSIGNED_INTEGER_TYPE = 'UNSIGNED_INTEGER'

class BapTransSchema(object):

    TABLE_NAME = 'baptrans'

    TIMESTAMP = 'timestamp'
    BAPPER = 'bapper'
    BAPPEE = 'bappee'
    BAPTYPE = 'baptype'

    columns = OrderedDict()
    columns[TIMESTAMP] = {'type': TIMESTAMPTZ_TYPE}
    columns[BAPPER] = {'type': TEXT_TYPE}
    columns[BAPPEE] = {'type': TEXT_TYPE}
    columns[BAPTYPE] = {'type': TEXT_TYPE}


class PlayersSchema(object):

    TABLE_NAME = 'players'

    NAME = 'name'
    JOIN_DATE = 'join_date'
    LEVEL = 'level'
    EXP = 'experience'

    columns = OrderedDict()
    columns[NAME] = {'type': TEXT_TYPE}
    columns[JOIN_DATE] = {'type': TIMESTAMPTZ_TYPE}
    columns[LEVEL] = {'type': UNSIGNED_INTEGER_TYPE}
    columns[EXP] = {'type': UNSIGNED_INTEGER_TYPE}


class LevelsSchema(object):

    TABLE_NAME = 'levels'

    LEVEL = 'level'
    EXP_NEEDED = 'exp_needed'
    DAILY_BAPS = 'daily_baps'
    DAILY_BAPS_POWER = 'daily_baps_power'
    DAILY_BAPS_SUPER = 'daily_baps_super'
    DAILY_BAPS_ULTRA = 'daily_baps_ultra'

    columns = OrderedDict()
    columns[LEVEL] = {'type': UNSIGNED_INTEGER_TYPE}
    columns[EXP_NEEDED] = {'type': UNSIGNED_INTEGER_TYPE}
    columns[DAILY_BAPS] = {'type': UNSIGNED_INTEGER_TYPE}
    columns[DAILY_BAPS_POWER] = {'type': UNSIGNED_INTEGER_TYPE}
    columns[DAILY_BAPS_SUPER] = {'type': UNSIGNED_INTEGER_TYPE}
    columns[DAILY_BAPS_ULTRA] = {'type': UNSIGNED_INTEGER_TYPE}
