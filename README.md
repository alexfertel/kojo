# Kojo's Kitchen

This is a simulation of the system described [here](docs/proyectos-eventos-discretos-2019.pdf).

## Getting Started

We have certain parameters that change the behaviour and therefore the results of this simulation. They may be found in the [config.py](config.py) file and you may change them as needed. One of them, the `MEAN` param, dictates how often customers arrive at our kitchen. Depending on this param, the measures requested will variate drastically.

After tweaking the parameters, we have two options:

* See the results of one simulation.

* See the results of `n` simulations.

For the first case, we may run the following:

```bash
./main.py one
```

Or, in case we want to see the performance of the system when adding an employee during peak hours:

```bash
./main.py 1
```

For the second case, 

