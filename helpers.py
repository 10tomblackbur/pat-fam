import os

import requests
import urllib.parse

#def lookup(symbol):
 #   """Look up quote for symbol."""

    # Contact API
#    try:
 #       api_key = os.environ.get("API_KEY")
  #      url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
   #     response = requests.get(url)
    #    response.raise_for_status()
#    except requests.RequestException:
 #       return None
#
 #   # Parse response
#    try:
#        quote = response.json()
#        return {
#            "'family': quote['family-id']"
#        }
#    except (KeyError, TypeError, ValueError):
#        return None

def find_family(doc_number, is_pub):
    # Look up pub/app number and return application numbers of all
    # applications in family

    # default search format is epodoc
    search_format = "epodoc"

    # check if publication or application number
    if is_pub:
        search_type = "publication"
    else:
        search_type = "application"
    


    