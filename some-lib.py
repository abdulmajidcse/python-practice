import os
import glob
import sys
import math
import random
import logging
from array import array

# get current directory
print('Current Directory:', os.getcwd());

# get all file list which are ends with .py
print('Python files:', glob.glob('*.py'))

# get current files paths
print('Current working files paths:', sys.argv)

# show error message
print(sys.stderr.write('Warning, log file not found starting a new one\n'))

print(math.pi)

print(random.choice(['apple', 'pear', 'banana']))

logging.error("Email or password are invalid!")

nums = array("H", [20, 40, 60])

print(type(nums))