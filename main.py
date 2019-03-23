#!/usr/bin/python3
from src.kitchen import Kitchen
from src.utils import set_env
from analysis.efficiency import analyze
from analysis.means import sample
from plots.exponential import plot as expoplot

import fire

def one(up=0):
    """
    :param: up - If truthy will simulate with `EMPLOYEES_COUNT + 1` employees.
    """
    from config import RUNS, LOG_FILE
    set_env("RUNS", RUNS + 1)

    k = Kitchen(up)
    k.run()

    with open(f"logs/{LOG_FILE}.txt") as f:
        print(f.read())

def more(n):
    """
    :param: n - Number of simulations to make.
    """
    analyze(n)

def results(mean):
    """
    :param: mean - `.csv` file to check, which is named after the `MEAN` param.
    """
    sample(mean)

def plot(name):
    expoplot(name)

if __name__ == "__main__":
    fire.Fire({
        "one": one,
        "more": more,
        "results": results,
        "expo": plot
    })

