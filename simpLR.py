from hypothesis import hypothesis
from cost import cost
import numpy as np

# data = np.loadtxt('ex1data2.txt', dtype='int', delimiter=',');
data = np.array([[1, 1],
                [2, 2],
                [3, 3]])

# data = np.array([[1, 0.5],
#                 [2, 1],
#                 [3, 1.5]])

X = data[::,0]
Y = data[::,-1]
print(X)
m = X.size

theta = np.random.rand(2)
theta = np.array([0, 1])
print("Original Theta: ", theta)
alpha = 0.01
j = 0
while True:
    j = j + 1
    print ("Epoch %d:" % (j))
    # Training Epoch
    hypotheses = hypothesis(m, 2, theta, X)
    print("hypotheses: ", hypotheses)
    c = cost(m, hypotheses, Y)
    print("Cost: ", c)
    if(c <= 0.01):
        print("Theta0 %f Theta1: %f" % (theta[0], theta[1]))
        break

    # Find derivative of cost function for theta 0 and theta 1
    sumError0 = 0
    sumError1 = 0
    for i in range(0,3):
        sumError0 += (hypotheses[i] - Y[i])
        sumError1 += (hypotheses[i] - Y[i]) * X[i]
    print("SumError0: ", sumError0)
    print("SumError1: ", sumError1)

    temp0 = theta[0] - (alpha * (1.0/m) * sumError0)
    temp1 =  theta[1] - (alpha * (1.0/m) * sumError1)
    theta[0] = temp0
    theta[1] = temp1

    print("New Theta: ", theta)
