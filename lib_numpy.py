import matplotlib.pyplot as plt
import numpy as np

def nump1():
    #a = np.array([1,2,3,4])
    a = np.zeros((3,3))
    b = np.ones((2, 5))
    c = np.random.random((4, 5))
    d = np.arange(0, 10, 2)
    e = np.linspace(0,1,10)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


def funk_x_2():
    x = np.linspace(-10, 10, 100)
    y = x**2

    plt.plot(x, y)
    plt.xlabel("X - Achse")
    plt.ylabel("Y - Achse")
    plt.grid(True)
    plt.show()

