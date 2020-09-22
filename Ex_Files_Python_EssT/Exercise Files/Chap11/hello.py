#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class MyString(str):
    def __str__(self):
        return self[::-1]


print("Hello, World.".upper())
print("Hello, World.".swapcase())
print(
    """
      Hello,
      World.

      {}

     """.format(
        42 * 7
    )
)
s = "Hello, World. {}"
print(s.format(42 * 7))
s = MyString("Hello, World")
print(s)

s1 = "Hello"
s2 = "World"
print(f"{s1:>10}, {s2:<10}")
