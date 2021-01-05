# Assignment from University of Michigan's Coursera Course Using Python to Access Web Data
# For this assignment, we must write a Python program to use urllib and Beautiful Soup to parse HTML, extract the link at the given pos,
# and follow that link, repeating the process count number of times to report the last name that we find. 
# Test with http://py4e-data.dr-chuck.net/known_by_Tyelor.html, letting count = 7 and position = 18. Answer is Erika. 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# data collection
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

print('Retrieving: %s' % url)

for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # getting anchor tags
    tags = soup('a') # list of all anchor tags
    ps = 0
    for tag in tags:
        ps += 1
        # if we reach the tag at the pos that we want, then
        if ps == pos:
            # we extract href values and now open up the link at that pos
            print('Retrieving: %s' % str(tag.get('href', None)))
            # we now reset the url to be that link, open the url, and again go to the url at the pos we want 
            url = str(tag.get('href', None))
            ps = 0
            break

    # repeat process count number of times
