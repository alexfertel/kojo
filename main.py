#!/usr/bin/python3
from src.kitchen import Kitchen
from analysis.efficiency import analyze

import sys

def main():
    up = 0
    if len(sys.argv) > 1:
        up = int(sys.argv[1])

    k = Kitchen(up)
    k.run()

def main1():
    import sys
    analyze(int(sys.argv[1]))

if __name__ == "__main__":
    main1()

