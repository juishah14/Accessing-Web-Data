# Assignment from Coursera's Accessing Web Data using Python
# For this assignment, we must write a Python program which will retrieve a web page over a socket and will only display content after the headers, from the web server.

# Prompt user for URL so any webpage can be read; socket program will only show data after the headers and a blank line have been received
# Test with http://data.pr4e.org/romeo.txt

import socket
url = input("Enter URL: ")

try: 
    # use split to break URL into its component parts, so that host name can be extracted for socket connect call
    host = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    # convert from Unicode to UTF-8 using encode()
    cmd = cmd.encode()
    mysock.send(cmd)

except:
    print("Invalid URL")
    exit()

# recv receives chars (including newlines), not lines
data = mysock.recv(1000)
# convert from UTF-8 to Unicode using decode()
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4  
print(message[header_end_pos:])
mysock.close()
