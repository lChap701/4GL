#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f"repr: The number of bunnies is {self._n}"

    def __str__(self):
        return f"str: The number of bunnies is {self._n}"


# print("Hello, World.")
# s = "Hello, World."
s = bunny(47)
print(repr(s))  # prints the representation of an object/variable
print(s)
print(ascii(s))
print(chr(128406))  # prints a value using unicode
print(ord("🖖"))  # prints the unicode for a specific value


# x = (1, 2, 3, 4, 5)
# x = ("cat", "dog", "rabbit", "velociraptor")
# for i, v in enumerate(x):
#    print(f"{i}: {v}")
# y = list(reversed(x))
# for i in y:
#    print(i)
# y = max(x)
# y = min(x)
# y = any(x)  # any() returns True when a tuple does not contain all 0s
# y = all(x)  # all() returns True when a tuple does not contain any 0s
# y = (6, 7, 8, 9, 10)
# z = zip(x, y)
# print(x)
# print(y)
# for a, b in z:
#    print(f"{a} - {b}")

x = 42
y = isinstance(x, int)
print(x)
print(y)