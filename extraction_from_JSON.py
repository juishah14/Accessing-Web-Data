# Assignment from University of Michigan's Coursera Course Using Python to Access Web Data
# For this assignment, we must read JSON data from the URL using urllib, parse and extract comment counts from JSON data,
# and compute the sum of the numbers in the file.
# Test with http://py4e-data.dr-chuck.net/comments_564448.json. Count will be 50 and sum will be 2306.

import urllib.request, urllib.parse, urllib.error
import json

# data collection
url = input('Enter URL: ')
# all data will be read and stored as one string in variable url_handle
url_handle = urllib.request.urlopen(url).read().decode() 

try:
    # js.loads() loads the string into the variable js as a dict which we can parse
    js = json.loads(url_handle) 
except:
    js = None

cn = 0 # count
sm = 0 # sum
for item in js['comments']:
    cn += 1
    sm += int(item['count'])

print('Count:', cn)
print('Sum:', sm)
