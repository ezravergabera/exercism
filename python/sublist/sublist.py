"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return 3

    if len(list_one) < len(list_two):
        length = len(list_one)
        if any((list_one == list_two[i:i+length]) for i in range(len(list_two)-length+1)):
            return 1

    if len(list_one) > len(list_two):
        length = len(list_two)
        if any((list_two == list_one[i:i+length]) for i in range(len(list_one)-length+1)):
            return 2

    return 4