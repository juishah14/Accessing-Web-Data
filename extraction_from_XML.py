# Assignment from Coursera's Accessing Web Data using Python
# For this assignment, we must read XML data from the given URL using urllib, parse and extract comment counts from XML data,
# and compute sum of numbers in the file.
# Test with http://py4e-data.dr-chuck.net/comments_564447.xml. Count will be 50 and sum will be 2451.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# data collection
url = input('Enter URL: ')
url_handle = urllib.request.urlopen(url, context=ctx)
data = url_handle.read().decode()
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

# creating XML tree and parsing it
tree = ET.fromstring(data) # making an XML tree of all elements
comment_lst = tree.findall('comments/comment') # this makes a list of all comments

count = len(comment_lst)
total_sum = 0
for x in comment_lst:
    total_sum += int(x.find('count').text)

# printing out sum and count
print('Count:', count)
print('Sum:', total_sum)
