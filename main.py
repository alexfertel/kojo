#!/usr/bin/python3
from src.kitchen import Kitchen
from src.utils import set_env
from analysis.efficiency import analyze
from analysis.means import sample
from analysis.parameterizer import explore_means, explore_food, explore
from plots.exponential import plot as expoplot
from plots.results import plot as resultsplot

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

def results(mean, food):
    """
    :param: mean - `.csv` file to check, which is named after a combination of the `MEAN` and `FOOD` params.
    :param: food - `.csv` file to check, which is named after a combination of the `MEAN` and `FOOD` params.
    """
    print(sample(mean, food))

def plot(name):
    """
    :param: name - Name of the file the plot is being saved.
    """
    expoplot(name)

def means(step_size=30, runs=100):
    """
    :param: step_size - Size of the step for the mean expxloration.
    :param: runs - Number of simulations.
    """
    explore_means(step_size, runs)

def food(runs=100):
    """
    :param: runs - Number of simulations.
    """
    explore_food(runs)

def mixed(runs=10):
    """
    :param: runs - Number of simulations.
    """
    explore(runs)

def three(): 
    resultsplot()

if __name__ == "__main__":
    fire.Fire({
        "one": one,
        "more": more,
        "results": results,
        "expo": plot,
        "means": means,
        "food": food,
        "mixed": mixed,
        "three": three,
    })

