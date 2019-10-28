import requests

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_BASE_URL']
    

def get_random_quote():
    '''
    Function that gets the response to our url request
    '''
    
    quote_data = requests.get(base_url)
    
    return quote_data