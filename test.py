import os

import requests
import urllib.parse
import sys

def main():
    # Get input from user - country code
    country_code = input("Country Code: ")

    # Check length of code
    country_code_len = len(country_code)
    if country_code_len != 2:
        print("Country Code must be two letters in length.")
        sys.exit()

    # Check code is characters from alphabet
    for j in range(country_code_len):
        if country_code[j].isalpha() == False:
            print("Country Code must only contain alphabetical characters.")
            sys.exit()

    # Convert to upper case
    country_code = country_code.upper()

    # Get input from user - app number
    app_number = input("Application Number: ")

    # Make sure app_number only has numerical characters
    for i in range(len(app_number)):
        if app_number[i].isdigit() == False:
            print("Application number must only contain numerical characters.")
            sys.exit()

    # Make request to get info from EPO
    res = requests.get(f"https://data.epo.org/linked-data/doc/application/{country_code}/{app_number}.json")
    res.status_code = int(res.status_code)

    # Check status code is good
    if res.status_code != 200:
        print("Invalid request.  Please enter a valid patent application number.")
        sys.exit()

    # Convert response to js object
    res_js = res.json()
    res.raise_for_status()

    # get url for the simple family for this patent
    try:
        family_url = res_js["result"]["primaryTopic"]["family"]["_about"] + ".json"
    except TypeError:
        print("Invalid request.  Please enter a valid patent application number.")
        sys.exit()
        
    # get info for this family and make it into js object
    family_res = requests.get(family_url)
    family_info = family_res.json()
    family_members = family_info["result"]["primaryTopic"]["familyMember"]

    # Print out countries/jurisdiction of each member
    for i in range(len(family_members)):
        print(family_members[i]["applicationAuthority"]["label"])


if __name__ == "__main__":
    main()
