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
    space_skip = False

    for letter in text:
        if space_skip and letter == " ":
            continue
        else:
            space_skip = False

        result += letter
        if letter in ".?:":
            result += "\n\n"
            space_skip = True

    print(result.strip())
