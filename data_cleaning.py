import pandas as pd
import logging

def data_cleaning(params):
    """
    This function cleans and organizes data in dataframes and write them to csv files. 
    If an error occurs while processing the data, the function logs the error message
    """
    if type(params[0]) == str:
        try:
            df = pd.read_json(params[0])
            flat_df = pd.json_normalize(df[params[1]])
            flat_df = flat_df.drop_duplicates(subset=['id'])
            flat_df['category_id'] = flat_df['id']
            flat_df['category_name'] = flat_df['name']
            flat_df['category_name'] = flat_df['category_name'].astype(str)
            flat_df['category_id'] = flat_df['category_id'].astype(int)
            flat_df.drop(['id', 'name', 'link'], axis=1, inplace=True)
            flat_df.to_csv(params[2][0], index=False)
        except Exception as e:
            logging.error(
                f"An error occurred while creating csv file {params[2][0]}: {e}")
    elif type(params[0]) == list:
        try:
            obj = {}
            obj['laptop_name'] = params[0]
            obj['quantity_sold'] = params[1]
            obj['unit_price'] = params[2]
            obj['shipping_cost'] = params[3]
            obj['store_name'] = params[4]
            obj['discount_percent'] = params[5]
            df = pd.DataFrame.from_dict(obj, orient='index')
            df = df.transpose()

            # create a series of numbers from 1 to the len of df for laptop_id
            df = df.assign(laptop_id=pd.Series(
                range(1, len(df)+1), dtype="int"))

            # Converting laptop_name from object type to string type
            df["laptop_name"] = df["laptop_name"].astype(str)

            df["quantity_sold"] = df["quantity_sold"].str.replace(
                '[^0-9]', '', regex=True)
            df["quantity_sold"] = df["quantity_sold"].fillna('0')
            df["quantity_sold"] = df["quantity_sold"].astype(int)

            df['unit_price'] = df['unit_price'].str.replace(
                '[^0-9.]', '', regex=True)
            df['unit_price'] = df['unit_price'].astype(float)

            df['shipping_cost'] = df['shipping_cost'].str.replace(
                'Free shipping', '0', regex=True)
            df['shipping_cost'] = df['shipping_cost'].str.replace(
                '[^0-9.]', '', regex=True)
            df['shipping_cost'] = df['shipping_cost'].astype(float)

            df['discount_percent'] = df['discount_percent'].str.replace(
                '[^0-9]', '', regex=True)
            df['discount_percent'] = df['discount_percent'].fillna('0')
            df['discount_percent'] = df['discount_percent'].astype(float)

            # create category_id column in df with default id of 702 (laptop)
            df = df.assign(category_id=702)

            # Placing laptop_id as the first column in  df
            laptop_id_col = df.pop('laptop_id')
            df.insert(0, 'laptop_id', laptop_id_col)

            laptop_df = df.copy()

            laptop_df.drop(['unit_price', 'quantity_sold',
                            'shipping_cost', 'discount_percent'], axis=1, inplace=True)

            laptop_df.to_csv("laptop.csv", index=False)

            # Drop rows where quantity is 0 in order to create sales tables
            for x in df.index:
                if df.loc[x, "quantity_sold"] == 0:
                    df.drop(x, inplace=True)

            df.drop(['store_name', 'category_id',
                     'laptop_name'], axis=1, inplace=True)

            df = df.assign(sales_id=pd.Series(
                range(1, len(df)+1), dtype="int"))

            first_col = df.pop('sales_id')
            df.insert(0, 'sales_id', first_col)

            sales_df = df.copy()
            sales_df.to_csv("sales.csv", index=False)
            print("Data is successfully extracted, cleaned and loaded into csv files.")
        except Exception as e:
            logging.error(f"An error occurred while cleaning or loading data into csv files: {e}")