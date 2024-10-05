#!/usr/bin/python3

"""this module that prints a text with 2 new lines
after each of these characters: ., ? and : """


def text_indentation(text):
    """
    this function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (string): text to be printed

    Returns:
        text with 2 new lines
        after each of these characters: ., ? and :

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for letter in text:
        result += letter
        if letter in ".?:":
            result += "\n\n"

    print(result.strip())
