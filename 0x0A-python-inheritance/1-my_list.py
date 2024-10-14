#!/usr/bin/python3
"""module for class MyList """


class MyList(list):
    """A class that extends the built-in list with a print_sorted method."""

    def print_sorted(self):
        """
        Prints the list in sorted order
        (without modifying the original list)

        """
        print(sorted(self))
