import matplotlib.pyplot as plt
import math
def solvedEquation(x, y):
    return x

def RK(h, iter, x_0, y_0):
    gradients = []
    for i in range(iter):
        a = solvedEquation(x_0, y_0)
        gradients.append(a)
        x_0+=h
        y_0+=a*h
    return gradients[0]

def main(h, x_0, y_0,iterations):
    coords = [[],[]]
    for i in range(iterations):
        coords[0].append(x_0)
        coords[1].append(y_0)
        try:
            a = solvedEquation(x_0, y_0)
            y_0+=h*a
        except:
            pass
        x_0+=h
    plot(coords)

def plot(arr):
    plt.plot(arr[0],arr[1])
    plt.show()

main(0.01,-50000, 0, 10000000)

