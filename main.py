#!/usr/bin/python3
from src.kitchen import Kitchen
from src.utils import set_env
from analysis.efficiency import analyze
from analysis.means import sample
from analysis.parameterizer import explore_means, explore_food
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
    """
    :param: name - Name of the file the plot is being saved.
    """
    expoplot(name)

def means(step_size=30, runs=100):
    explore_means(step_size, runs)

def food(runs=100):
    explore_food(runs)

if __name__ == "__main__":
    fire.Fire({
        "one": one,
        "more": more,
        "results": results,
        "expo": plot,
        "means": means,
        "food": food,
    })

