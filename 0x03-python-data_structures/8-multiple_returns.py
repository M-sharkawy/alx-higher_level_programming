#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return None
    elif len(sentence) == 0:
        return (0, None)
    else:
        lenght = len(sentence)
        f_char = sentence[0]
        return(lenght, f_char)
