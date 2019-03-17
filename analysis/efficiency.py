from src.kitchen import Kitchen
from config import LAMBDA

config_file = "config.py"

def set_env(var, value):
    f = open(config_file)
    lines = f.readlines()
    f.close()

    f = open(config_file, "w")
    for line in lines:
        if line.startswith(var):
            if type(value) is str:
                f.write(f'{var}\t\t= "{value}"\n')
            else:
                f.write(f'{var}\t\t\t= {value}\n')
        else:
            f.write(line)
    f.close()

def get_env(var):
    f = open(config_file)
    lines = f.readlines()
    f.close()

    r = None
    f = open(config_file, "r")
    for line in lines:
        if line.startswith(var):
            r = line.split('=')[1].strip()
    f.close()
    return r

def analyze(runs):
    print(f"Lambda is {LAMBDA}")
    for i in range(runs):
        # Compute next log file
        index = int(get_env("RUNS")) + 1

        log_file = f"kitchen_{index}"
        set_env("LOG_FILE", log_file)

        # Normal Kitchen
        kdown = Kitchen()  # `EMPLOYEES_COUNT` employees.
        kdown.run()
        
        # Process results from kdown
        more_than_five = [1 if t >= 300 else 0 for t in kdown.deltas]
        pdown = (sum(more_than_five) * 100) / len(more_than_five)
        print(f"Simulation {i}\tpercent of clients who waited more than 5 minutes in type `down` is\t{pdown}")

        # With three employees
        kup = Kitchen(upgraded=1)  # `EMPLOYEES_COUNT + 1` employees.
        kup.run()

        # Process results from kup
        more_than_five = [1 if t >= 300 else 0 for t in kup.deltas]
        pup = (sum(more_than_five) * 100) / len(more_than_five)
        print(f"Simulation {i}\tpercent of clients who waited more than 5 minutes in type `up` is\t{pup}")

        # Update `RUNS` env var
        set_env("RUNS", index)

if __name__ == "__main__":
    print("Hi")