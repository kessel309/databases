from .models import Gist

# <REMOVE ME - FROM HERE
DATETIME_PREFIXES = ('created_at', 'updated_at')


def is_datetime_param(param):
    for prefix in DATETIME_PREFIXES:
        if param.startswith(prefix):
            return True
    return False


def get_operator(comparison):
    return {
        'lt': '<',
        'lte': '<=',
        'gt': '>',
        'gte': '>=',
    }[comparison]


def build_query(**kwargs):
    # This is UGLY as fuck. Please remove.
    query = 'SELECT * FROM gists'
    values = {}
    if kwargs:
        filters = []
        for param, value in kwargs.items():
            if is_datetime_param(param):
                attribute, comparison = param.split('__')
                operator = get_operator(comparison)
                filters.append(
                    'datetime(%s) %s datetime(:%s)' % (
                        attribute, operator, param))
                values[param] = value
            else:
                filters.append(
                    '%s = :%s' % (
                        param, param))
                values[param] = value

        query += ' WHERE '
        query += ' AND '.join(filters)

    return query, values

# REMOVE ME - TO HERE />

def search_gists(db_connection, **kwargs):
    pass