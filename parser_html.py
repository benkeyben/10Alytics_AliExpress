from bs4 import BeautifulSoup

def parser_html(response, tag, attribute):
    """
    This function parses the HTML content of the response 
    and returns a list of text data for the specified HTML 
    tag and class attribute. If an error occurs while parsing 
    the HTML content, the function logs the error message. 
    """
    if response is None:
        return None
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        data_list = soup.find_all(tag, class_=attribute)
        return [data.text for data in data_list]
    except Exception as e:
        logging.error(f"An error occurred while parsing HTML content: {e}")
        return None
        