#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = "This is a long string with a bunch of words in it."
print(s)

# Splits every letter
print(s.split())
l = s.split()

# Combines the list of letters and sperates each word with ":"
s2 = ":".join(l)
print(s2)

# Splits on every "i"
print(s.split("i"))