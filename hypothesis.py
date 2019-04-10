import numpy as np

def hypothesis(m, n, theta, X):
    hypotheses = np.zeros(m, dtype='float')
    for i in range(0, m):
        hyp = 0
        for j in range(0, n):
            hyp += (theta[j] * X[j])
            print(hyp)
        hypotheses[i] = hyp
    return hypotheses
