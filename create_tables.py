def create_tables(sql_stmt_list, conn):
    """
    This function executes the sql statement 
    object to create tables and schema and closes the
    connection. It accepts sql statements list, and database
    connection object
    """
    cursor = conn.cursor()
    for stmt in sql_stmt_list[0]:
        cursor.execute(stmt)
    conn.commit()
