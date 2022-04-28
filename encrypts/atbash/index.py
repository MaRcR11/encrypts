from string import ascii_lowercase
import sys


def main(argv):
    print("Input:", argv[0].lower())
    argv = list(argv[0].lower())
    j = 0
    try:
        while j < len(argv):
            argv[j] = list(ascii_lowercase)[25 - ascii_lowercase.index(argv[j])]
            j += 1
    except ValueError:
        print("Error: You entered something that was not type of char")
        return

    print("Output:", "".join(argv))


if __name__ == "__main__":
    main(sys.argv[1:])
