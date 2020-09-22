#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    # animals = {
    #    "kitten": "meow",
    #    "puppy": "ruff!",
    #    "lion": "grrr",
    #    "giraffe": "I am a giraffe!",
    #    "dragon": "rawr",
    # }
    animals = dict(
        kitten="meow",
        puppy="ruff!",
        lion="grrr",
        giraffe="I am a giraffe!",
        dragon="rawr",
    )
    # Prints all keys in the dictionary
    # for k in animals.keys():
    #    print(k)

    # Prints all values in the dictionary
    # for v in animals.values():
    #    print(v)

    # Prints the value of the key "lion"
    # print(animals["lion"])

    # Assigns a new value to the key "lion"
    # animals["lion"] = "I am a lion"

    # Prints "True" since the dictionary contains a key called "lion"
    # print("lion" in animals)

    # Prints "found!" since the dictionary contains a key called "lion"
    # print("found!" if "lion" in animals else "nope!")

    # Prints "nope!" since the dictionary does not contains a key called "godzilla"
    # print("found!" if "godzilla" in animals else "nope!")

    # Causes a KeyError exception since the key doesn't exist
    # print(animals["godzilla"])

    # Returns "None" since the key doesn't exist
    # print(animals.get("godzilla"))

    print_dict(animals)


def print_dict(o):
    # for x in o:
    #    print(f"{x}: {o[x]}")
    for k, v in o.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
