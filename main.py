#!/usr/bin/python3
from tests import expogen
from src.kitchen import Kitchen

def main():
    k = Kitchen()
    k.run()

def tests():
    print(list(expogen.itShouldGenerateExponentialRandomVariables(1)))

if __name__ == "__main__":
    main()

