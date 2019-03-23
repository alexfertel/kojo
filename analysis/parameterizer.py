from src.utils import get_env, set_env
from .efficiency import analyze

import numpy as np

def explore_means(step_size=30, runs=100):
    assert 5 <= step_size <= 120, "Step size should be between 5 and 120."
    for i in np.arange(60, 901, step_size):
        set_env("MEAN", i)

        analyze(runs)

def explore_food(runs=100):
    for i in np.arange(0, 1, .05):
        set_env("FOOD", i)

        analyze(runs, round(i, 2) * 100)



