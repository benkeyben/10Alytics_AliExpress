from parser_html import parser_html
import requests

def request_html_data(params):
    """
    This function retrieves the HTML content of the website, 
    and then calls the parse_html function to extract the 
    relevant information. The information is returned as a list of lists
    """
    start = params['webpages']['start']
    end = params['webpages']['end']
    tags = params['tags']
    attributes = params['attributes']
    all_list = params['all_list']
    for num in range(start, end):
        try:
            response = requests.get(params['urls'][1])
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
            break
        else:
            print(
                f"Response is sucessful. Extracting html data from webpage {num}.")
            for i in range(0, len(tags)):
                all_list[i] += parser_html(response, tags[i], attributes[i])
            url = f'https://www.aliexpress.com/w/wholesale-laptop.html?page={num+1}&g=y&SearchText=laptop'
    return all_list