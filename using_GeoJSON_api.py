# Assignment from Coursera's Accessing Web Data using Python
# For this assignment, we will use the GeoLocation Lookup API, which is modelled after the Google API, to look up universities and parse the
# returned data.

# The program will prompt for a location, contact a web service, and retrieve JSON for the web service , parse that data, and retrieve
# the first place_id from the JSON file. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# Test with location South Federal University to get ChIJy0Uc1Zmym4gR3fmAYmWNuac as place id

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy.....IDByT70'

if api_key is False:
    # Using API endpoint that has a static subset of Google Data. This API uses the same parameter (address) as the Google API.
    # Note- this API has no rate limit, so can test as often as you like. 

    # If you visit the URL with no parameters, you will get a "No address..." response.
    # To call the API, must include a key= parameter and provide the address that you are requesting as the address= parameter
    # to urllib.parse.urlencode(), so that it can properly encode the URL. 

    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # creating a url 
    # the urlib.parse part encodes the address properly so that it can be concatenated to the end of the service url
    # it will encode it to look something like address=Ann+Arbor%2C+MI if you give the address Ann Arbor, MI
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    # opening url and getting a handle back; reading data from handle and
    # decoding that data from UTF-8 to Unicode and saving it in a string data
    url_handle = urllib.request.urlopen(url, context=ctx)
    # all data stored as one string in variable data
    data = url_handle.read().decode() 
    print('Retrieved', len(data), 'characters')

    try:
        # parsing that string (data that we got back from Google API) to now store all data in that as a dict (js is a dict)
        js = json.loads(data) 
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to Receive Location')
        continue

    # Optional: to see all raw data at once
    # print(json.dumps(js, indent=4))

    place_id = js['results'][0]['place_id']
    print(place_id)