import psycopg2

def db_connect(params):
    """
    This function creates a connection to the database using the
    parameter passed into it and returns the connection object
    """
    conn = psycopg2.connect(
        database=params['database'],
        user=params['user'],
        password=params['password'],
        host=params['host'],
        port=params['port']
    )
    return conn



