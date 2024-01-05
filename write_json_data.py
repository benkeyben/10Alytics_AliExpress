import json
import logging

def write_json_data(params, data):
    """
    This function writes json data to a specific file. 
    If an error occurs while writing the data, the function 
    logs the error message
    """
    filename = params['filenames'][0]
    try:
        with open(filename, 'w') as json_file:
            print(f"Response is sucessful. Writing json data to {filename}.")
            json.dump(data, json_file)
    except Exception as e:
        logging.error(f"An error occurred while saving data: {e}")
