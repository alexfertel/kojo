#!/usr/bin/python3
from tests import expogen
from src.kitchen import Kitchen

import sys

def main():
    up = 0
    if len(sys.argv) > 1:
        up = int(sys.argv[1])

    k = Kitchen(up)
    k.run()

def tests():
    print(list(expogen.itShouldGenerateExponentialRandomVariables(1)))

if __name__ == "__main__":
    main()

