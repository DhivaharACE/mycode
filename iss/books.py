#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Accessing Open APIs with Python"""

# standard library
import json

# 3rd party library
import requests

# Define URL as a global constant (this will not change)
MAJORTOM = 'https://anapioficeandfire.com/api/books'

def main():
    """making API requests"""
    
    # Call the web service
    resp = requests.get(MAJORTOM)  # sends an HTTP GET
    
    # strip JSON data off response and convert
    # to python data types
    data = resp.json()
            
    # for-loop across astros
    # display book names
    for x in data:
        print("Book name is", x['name'])

if __name__ == '__main__':
    main()

