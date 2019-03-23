from src.kitchen import Kitchen
from src.utils import get_env, set_env

def analyze(runs, prefix="kitchen"):
    mean = int(get_env("MEAN"))
    print(f"1 / Lambda is {mean / 60} minutes")
    for i in range(runs):
        # Compute next log file
        index = int(get_env("RUNS")) + 1

        log_file = f"{prefix}_{index}"
        set_env("LOG_FILE", log_file)

        # Normal Kitchen
        kdown = Kitchen()  # `EMPLOYEES_COUNT` employees.
        kdown.run()
        
        # Process results from kdown
        more_than_five = [1 if t >= 300 else 0 for t in kdown.deltas]
        pdown = (sum(more_than_five) * 100) / len(more_than_five)
        print(f"Simulation {i}:\tCustomers who waited > 5 minutes in a normal   kitchen\t% {pdown}")

        # With three employees
        kup = Kitchen(upgraded=1)  # `EMPLOYEES_COUNT + 1` employees.
        kup.run()

        # Process results from kup
        more_than_five = [1 if t >= 300 else 0 for t in kup.deltas]
        pup = (sum(more_than_five) * 100) / len(more_than_five)
        print(f"Simulation {i}:\tCustomers who waited > 5 minutes in a upgraded kitchen\t% {pup}")

        # Update `RUNS` env var
        set_env("RUNS", index)
    
        # Save results
        with open(f"results/{mean}{'_' + str(prefix) if str(prefix) != 'kitchen' else ''}.csv", "a") as fd:
            fd.write(f"{pdown},{pup}\n")
