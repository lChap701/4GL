#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

    # Sorts variables and prints it
    print_set(sorted(a))
    print_set(sorted(b))

    # Gets the characters that are only in one of the sets
    print_set(a - b)

    # Prints all the characters in at least one of the sets
    print_set(a | b)

    # Prints all the characters in only one of the sets
    print_set(a ^ b)

    # Prints all the characters in both sets
    print_set(a & b)

def print_set(o):
    print("{", end="")
    for x in o:
        print(x, end="")
    print("}")


if __name__ == "__main__":
    main()
