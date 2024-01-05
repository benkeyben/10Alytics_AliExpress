# sql_stmt_list is a list of sql statements to create schema and tables and insert
sql_stmt_list = [
    [
        "DROP DATABASE IF EXISTS AliExpress;",
        "CREATE AliExpress;",
        """CREATE SCHEMA lap;""",
        """
        CREATE TABLE IF NOT EXISTS lap.category (
            category_id INTEGER PRIMARY KEY,
            category_name VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS lap.laptop (
            laptop_id SERIAL PRIMARY KEY,
            laptop_name VARCHAR(255),
            store_name VARCHAR(255), 
            category_id INTEGER
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS lap.sales (
            sales_id SERIAL PRIMARY KEY,
            laptop_id INTEGER,
            unit_price DECIMAL(10, 2),
            quantity_sold INTEGER, 
            discount_percent DECIMAL(10, 2),
            shipping_cost DECIMAL(10, 2),
            FOREIGN KEY (laptop_id) REFERENCES lap.laptop(laptop_id)
        );
        """
    ],
    [
        "INSERT INTO lap.category (category_id,category_name) VALUES (%s, %s);",
        """INSERT INTO lap.laptop (laptop_id,laptop_name,store_name,category_id) VALUES (%s, %s, %s, %s);""",
        """INSERT INTO lap.sales (sales_id,laptop_id,quantity_sold,unit_price,discount_percent,shipping_cost) VALUES (%s, %s, %s, %s, %s, %s);"""
    ]
]