from src.expogen import Exp
import numpy as np

def itShouldGenerateExponentialRandomVariables(lamb):
    results = [f for f in np.arange(.01, 1, .01)]
    
    e = Exp(lamb)
    return map(lambda f: e.inverse(f), results)

if __name__ == "__main__":
    print(list(itShouldGenerateExponentialRandomVariables(1)))