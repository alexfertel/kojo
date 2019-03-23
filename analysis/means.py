#!/usr/bin/python3
def sample(mean, food=50):
    sample_mean = 0
    with open(f"results/{mean}{'_' + str(round(food * 100, 2))}.csv") as fd:
        length = 0
        for line in fd.readlines():
            pdown, pup = line.strip().split(',')
            sample_mean += float(pdown) - float(pup)
            length += 1
        sample_mean /= length

        print(sample_mean)
    return sample_mean

if __name__ == "__main__":
    import sys
    sample(sys.argv[1])
