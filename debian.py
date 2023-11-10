import urllib, math

from urllib.request import urlopen

response = urlopen('http://www.debian.org')

response

response.readline()