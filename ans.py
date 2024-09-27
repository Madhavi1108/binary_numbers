#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b = bin(n)
    binary = b[2:]

    output = re.findall(r'1+', binary)
    print(len(max(output)))

