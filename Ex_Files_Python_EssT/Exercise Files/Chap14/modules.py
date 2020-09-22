#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random


def main():
    # v = sys.version_info
    # print("Python version {}.{}.{}".format(*v))
    # v = sys.platform
    # v = os.name
    # v = os.getenv("PATH")
    # v = os.getcwd()
    # v = os.urandom(25)    # gets a random binary number from 1 to 25
    # v = os.urandom(25).hex()  # gets a random number from 1 to 25 in hexidecimal
    # print(v)
    # x = random.randint(1, 1000)
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)


if __name__ == "__main__":
    main()
