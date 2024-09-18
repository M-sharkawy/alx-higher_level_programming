#!/usr/bin/python3


if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    if sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
    
    operators = { "+" : add, "-" : sub, "*" : mul, "/" : div}

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b,  operators[sys.argv[2]](a, b)))