#!/usr/bin/python3
def sample(lamb):
    with open(f"results/{lamb}.csv") as fd:
        sample_mean = 0
        length = 0
        for line in fd.readlines():
            pdown, pup = line.strip().split(',')
            sample_mean += float(pdown) - float(pup)
            length += 1
        sample_mean /= length

        print(sample_mean)

if __name__ == "__main__":
    import sys
    sample(sys.argv[1])
