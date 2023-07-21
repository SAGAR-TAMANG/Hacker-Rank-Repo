
import math
import os
import random
import re
import sys



n = int(input().strip())

rem = n%2

if rem == 0:
    if n in range(2,6):
        print('Not Weird')
    elif n in range(6,21):
        print('Weird')
    elif n > 20:
        print('Not Weird')
    else:
        print('Weird')
