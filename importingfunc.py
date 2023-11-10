import os
os.system("clear")

# many functions are only available via "import" from outside libraries
# libraries my be installed with python or downloaed from an internet resource
# python package index, pypi (https://pypi.org)

# imported functions must be installed at the top of your script!!

import fileinput

# make an alias to fileinput
# import fileinput as fi

# use fileinput's input() function
lines = fileinput.input()

# use alias
# lines = fi.input()

# use build-in input() function
# data = input()

# included with python but need to call it
import time
print(time.time())
print(time.localtime())
print(time.asctime())

# install numpy
# https://numpy.org/install
# pip3 install numpy

import numpy

numpyArray = numpy.array([9,5,7,100])

# to make HTTP requests
# pip3 install requests
# import requests