#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    expected_arg_count = 3
    if len(sys.argv) - 1 != expected_arg_count:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[3])
    result = ops[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
