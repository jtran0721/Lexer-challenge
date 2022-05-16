import json
from multiprocessing.sharedctypes import Value
import os
from token import EQUAL
import requests
import urllib

#Function to find url contain 789
def find(key):
    link = requests.get("https://jsonplaceholder.typicode.com/photos") #This will get the link to the json file
    text = link.text # Open the file in text
    data = json.loads(text) # load this text to json format
    output = [] # An empty list to store output 
    for item in data: # This will go through every item in the json list
        if key in item["url"]: # Find the key that contains "789" in each item
            output.append(item['url']) # Put the result into the empty list above so it can be used later
    return output

#Function to dowload images
def download(key):
    list = find(key) # Call the function above so it can retrieve the list of the links
    for image in list: # Then go through each link in the list
        file_name = image.split('/')[-1] + ".png" # set the file name as the last string in the url with png as extension
        r = requests.get(image, stream=True) # Request for the images
        with open(file_name, 'wb') as f: # open empty file 
            for chunk in r:
                f.write(chunk) # then save it locally
    return None


print(download("789"))