import requests
import logging

def request_json_data(params):
    """
    This function retrieves json data from 
    the specified URL. If an error occurs while
    retrieving the data, the function 
    logs the error message
    """
    url = params['urls'][0]
    headers = params['headers']
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except Exception as e:
        logging.error(
            f"An error occurred while retrieving data from {url}: {e}")
        return None
