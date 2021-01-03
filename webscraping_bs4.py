# Assignment from Coursera's Accessing Web Data using Python
# For this assignment, we must write a Python program to use urllib and Beautiful Soup to parse HTML, 
# scrape/extract numbers from the file, and compute their sum.
# Test with http://py4e-data.dr-chuck.net/comments_564445.html. Answer is 2552.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# returns entire document at that web page
html = urlopen(url, context=ctx).read()
# creating soup object
soup = BeautifulSoup(html, "html.parser")

sum = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])
    
print(sum)
