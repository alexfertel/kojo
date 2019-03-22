# Kojo's Kitchen

This is a simulation of the system described [here](docs/proyectos-eventos-discretos-2019.pdf).

## Getting Started

We have certain parameters that change the behaviour and therefore the results of this simulation. They may be found in the [config.py](config.py) file and you may change them as needed. One of them, the `MEAN` param, dictates how often customers arrive at our kitchen. Depending on this param, the measures requested will variate drastically.

After tweaking the parameters, we have three options:

* See the results of one simulation.

* See the results of `n` simulations.

* See the results for a specific `MEAN` parameter.

For the first case, we may run the following:

```bash
./main.py one
```

Or, in case we want to see the performance of the system when adding an employee during peak hours:

```bash
./main.py one 1
```

For the second case, when we run `n` simulations, one after another:

```bash
./main.py more
```

This will run one simulation for a *normal* kitchen and one for an *upgraded* kitchen, where upgraded is a kitchen with an extra employee during peak hours.

Then we have a third desirable case, which is to see the error for the requested measure, i.e., how much better is adding an extra employee when running `n` simulations. For this case we have the following syntax:

```bash
./main.py results (MEAN)
```

Where the parameter `MEAN` means the **frequency** customers arrive at the kitchen in seconds. That is, to analyse what happens when we set the frequency to 5 minutes. We modify the variable `MEAN` and set it to `300` in `config.py`, then run `n` simulations and finally ask for results, like this:

```bash
./main.py results 300
```
