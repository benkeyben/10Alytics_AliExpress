from create_tables import create_tables
from data_cleaning import data_cleaning
from db_connection import db_connect
from request_html_data import request_html_data
from insert_data import insert_data
from parser_html import parser_html
from request_json_data import request_json_data
from sql_stmt_lists import sql_stmt_list
from write_json_data import write_json_data

def main():
    """
    This function executes the other
    functions and regulate the whole program
    """
    params = {
        'database': 'AliExpress',
        'user': 'postgres',
        'password': 'password',
        'host': 'localhost',
        'port': 5432,
        'table_names': ['lap.category', 'lap.laptop', 'lap.sales'],
        "filenames": ['categories.json', 'categories', ['category.csv', 'laptop.csv', 'sales.csv']],
        'urls': [
                    "https://ali-express1.p.rapidapi.com/categories",
                    "https://www.aliexpress.com/w/wholesale-laptop.html?g=y&SearchText=laptop"
        ],
        'headers': {
            "X-RapidAPI-Key": "evebndjdudbevst12fbeh53749gshsjbbsn_wbw",
            "X-RapidAPI-Host": "ali-express1.p.rapidapi.com"
        },
        'webpages': {
            'start': 1,
            'end': 5
        },
        # The length of the tags list must be the same as the length of the corresponding attributes list
        'tags': ["h1", "span", "div", "span", "span", "span"],
        'attributes': [
            "multi--titleText--nXeOvyr",
            "multi--trade--Ktbl2jB",
            "multi--price-sale--U-S0jtj",
            "tag--text--1BSEXVh tag--textStyle--3dc7wLU multi--serviceStyle--1Z6RxQ4",
            "cards--store--3GyJcot",
            "tag--text--1BSEXVh tag--textStyle--3dc7wLU multi--superStyle--1jUmObG"
        ],
        # The length of the all_list must be the same as the length of tags or attributes
        'all_list': [[], [], [], [], [], []]
    }

    json_data = request_json_data(params)
    if json_data is not None:
        write_json_data(params, json_data)
        data_cleaning(params['filenames'])

    all_list = extract_html_text(params)
    data_cleaning(all_list)
    connection = db_connect(params)
    create_tables(sql_stmt_list, connection)
    insert_data(params, connection, sql_stmt_list)

main()
