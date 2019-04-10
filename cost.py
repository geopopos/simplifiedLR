import math

def cost (m, hypothesis, actual):
    error_squared = 0;
    for hypo, act in zip(hypothesis, actual):
        error_squared = error_squared + math.pow((hypo - act), 2)
    return (1.0/(2.0*m)) * error_squared
