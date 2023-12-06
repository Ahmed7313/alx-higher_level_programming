#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    argument_word = "argument" if count == 1 else "arguments"
    print(f"{count} {argument_word}{'.' if count == 0 else ':'}")

    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")
