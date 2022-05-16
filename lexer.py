import json
from multiprocessing.sharedctypes import Value
import os
from token import EQUAL
import requests
import urllib

#Function to find url contain 789
def find(key):
    link = requests.get("https://jsonplaceholder.typicode.com/photos")
    text = link.text
    data = json.loads(text)
    output = []
    for item in data:
        if key in item["url"]:
            output.append(item['url'])
    return output

#Function to dowload images
def download():
    list = find('789')
    for image in list:
        file_name = image.split('/')[-1]
        r = requests.get(image, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    return None


print("Download completed")