from random import choice
from string import ascii_lowercase
import sys


def main(argv):
    opt = False
    default = True
    frequencyCharEnglish = []
    print("Input:", argv[0])
    if len(argv) > 2:
        print("Please enter {INPUT} {option}")
        return
    if len(argv) == 1:
        default = True
    if len(argv) == 2:
        if argv[1] != "-e" and argv[1] != "-g":
            print("Please chose as an option -g or -e ")
            return
        opt = argv[1]

    nums = [i for i in range(100)]

    if opt == "-g" or default:
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
    if opt == "-e":
        frequencyCharEnglish = [
            7,
            1,
            2,
            4,
            12,
            1,
            1,
            5,
            7,
            1,
            1,
            4,
            3,
            7,
            8,
            2,
            1,
            6,
            6,
            10,
            3,
            1,
            3,
            1,
            2,
            1,
        ]

    assignedNums = []
    y = []
    frequencyCharChosen = frequencyCharEnglish or frequencyCharGerman

    for j in frequencyCharChosen:
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
            print("ValueError: You entered something that was not type of char")
            return

    print("Output:", charEncrypted)


if __name__ == "__main__":
    main(sys.argv[1:])
