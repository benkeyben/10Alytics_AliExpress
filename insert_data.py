import csv
import logging

def insert_data(params, conn, sql_stmt_list):
    """
    This function loads the data in csv files into their repective tables in
    the database postgres. It accepts a list of csv files, connection object
    and sql statement parameters
    """
    sql_stmt = sql_stmt_list[1]
    cursor = conn.cursor()
    print("Loading data into tables in database.")
    for i, csv_file in enumerate(params['filenames'][2]):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # skip the header row
                for row in reader:
                    cursor.execute(sql_stmt[i], row)
            print(f"Finished loading data into {params['table_names'][i]} tables")
        except Exception as e:
            logging.error(f"An error occurred while loading data into {params['table_names'][i]} tables: {e}")
    conn.commit()
    cursor.close()
    conn.close()