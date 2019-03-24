# Kojo's Kitchen

This is a simulation of the system described [here](docs/proyectos-eventos-discretos-2019.pdf). We discuss the model an the results [here](paper/paper.pdf).

## Getting Started

You must have installed [fire](https://github.com/google/fire) in order to run this project or build the docker image and then, follow the [docker](#Docker) section.

We have certain parameters that change the behaviour and therefore the results of this simulation. They may be found in the [config.py](config.py) file and you may change them as needed. Two of them, the `MEAN` and the `FOOD` params, dictate how often customers arrive at our kitchen and which proportion of customers prefer sandwiches. Depending on these params, the measures requested will variate drastically.

After tweaking the parameters, we have the next options:

* See the results of one simulation.

    For the first case, we may run the following:

    ```bash
    python3 main.py one
    ```

    Or, in case we want to see the performance of the system when adding an employee during peak hours:

    ```bash
    python3 main.py one 1
    ```

* See the results of `n` simulations.

    For the second case, when we run `n` simulations, one after another:

    ```bash
    python3 main.py more
    ```

    This will run one simulation for a *normal* kitchen and one for an *upgraded* kitchen, where upgraded is a kitchen with an extra employee during peak hours.

* See the results for specific pairs of `MEAN` and `FOOD` parameters.

    Then we have a third desirable case, which is to see the error for the requested measure, i.e., how much better is adding an extra employee when running `n` simulations. For this case we have the following syntax:

    ```bash
    python3 main.py results (MEAN) (FOOD)
    ```

    Where the parameter `MEAN` is the **frequency** customers arrive at the kitchen in seconds. That is, to analyse what happens when we set the frequency to 5 minutes. The `FOOD` param is the **proportion** of customers that prefer
    sandwiches, i.e. how many customers rather have sandwich from 100 persons. We modify both variables and set them in `config.py`, then run `n` simulations and finally ask for results, like this:

    ```bash
    python3 main.py results 60 0.5
    ```

* See a plot of the exponential variable generator.

    ```bash
    python3 main.py expo
    ```

* Explore the space of the `MEAN` parameter.

    We can explore the space of means between 1 an 11 minutes, giving a `step_size`
    param.

    ```bash
    python3 main.py means [step_size]
    ```

* Explore the space of the `FOOD` parameter.

    We can explore the space of the proportion between 0 and 100 of the amount of people who prefer sandwiches over sushi.

    ```bash
    python3 main.py food
    ```

* Explore the space of the `FOOD` and `MEAN` parameters.

    We can explore the space of both parameters.

    ```bash
    python3 main.py mixed
    ```

* See a 3D plot of the results.

    ```bash
    python3 main.py three
    ```

### Docker

In order to run this project, if you don't have [fire](https://github.com/google/fire), then build the image with:

```bash
docker build -t alexfertel/kojo:latest .
```

And then just run:

```bash
docker run --rm alexfertel/kojo [command]
```

Where `command` is just one of the above, just like:

```bash
docker run --rm alexfertel/kojo more
```
