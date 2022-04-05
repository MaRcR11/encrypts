from random import choice
from string import ascii_lowercase
import sys, getopt


def main(argv):

    print("Input:", argv[0])

    if len(argv) != 1:
        return
    nums = [i for i in range(100)]

    frequencyCharGerman = [
        6,
        2,
        2,
        5,
        17,
        2,
        3,
        5,
        8,
        1,
        1,
        3,
        2,
        10,
        2,
        1,
        1,
        7,
        7,
        6,
        4,
        1,
        1,
        1,
        1,
        1,
    ]

    assignedNums = []
    y = []

    for j in frequencyCharGerman:
        while j > 0:
            x = choice(nums)
            nums.remove(x)
            y.append(x)
            j = j - 1
            if j == 0:
                assignedNums.append(y)
                y = []

    charToEncrypt = argv[0]

    charEncrypted = ""

    for i in charToEncrypt:
        try:
            alphaPos = ascii_lowercase.index(i)
            x = str((choice(assignedNums[alphaPos])))
            charEncrypted += x
        except ValueError:
            print(
                "You entered something containing numbers... Do not do this. Only enter something of type string."
            )
            return

    print("Output:", charEncrypted)


if __name__ == "__main__":
    main(sys.argv[1:])
