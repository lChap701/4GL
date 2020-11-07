#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    infile = open("lines.txt", "rt")
    outfile = open("lines-copy.txt", "wt")
    for line in infile:
        # print(line.rstrip(), file=outfile)    # will interpret line endings for the OS
        outfile.writelines(line)  # will not inperpret line endings
        print(".", end="", flush=True)
    outfile.close()
    print("\ndone.")


if __name__ == "__main__":
    main()
