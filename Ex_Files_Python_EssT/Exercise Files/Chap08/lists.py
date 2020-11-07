#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    game = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    # Prints the 2nd value in the list
    # print(game[1])

    # Prints the 2nd and 3rd value in the list
    # print(game[1:3])

    # Prints the 2nd and 4th value in the list
    # print(game[1:5:2])

    # Gets index of an item
    # i = game.index("Paper")

    # Displays the item using it's index
    # print(game[i])

    # Inserts "Computer" to the start of the list
    # game.insert(0, "Computer")
    # game.append(0, "Computer")

    # Removes a value
    # game.remove("Paper")

    # Removes the last value in the list and prints the value that was removed
    # x = game.pop()
    # print(x)

    # Removes the 4th value in the list and prints the value that was removed
    # x = game.pop(3)
    # print(x)

    # Removes the 4th value in the list
    # del game[3]

    # Removes the 2nd and 3rd value in the list
    # del game[1:3]

    # Removes the 2nd and 4th value in the list
    # del game[1:5:2]

    # Adds a seperator for list of values
    # print(", ".join(game))

    # Prints the amount of items in the list
    print(len(game))

    print_list(game)


def print_list(o):
    for i in o:
        print(i, end=" ", flush=True)
    print()


if __name__ == "__main__":
    main()
