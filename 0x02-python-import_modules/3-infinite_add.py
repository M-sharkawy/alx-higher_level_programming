#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    sum = 0
    for arg in args:
        sum += int(arg)
    print(sum)
