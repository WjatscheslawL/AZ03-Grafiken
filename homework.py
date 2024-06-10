import matplotlib.pyplot as plt
import numpy as np


def aufgabe1():
    mean = 0
    std_dev = 1
    num_samples = 1000
    data = np.random.normal(mean, std_dev, num_samples)
    plt.hist(data, bins=6)
    plt.title("гистограмма для случайных данных")
    plt.xlabel("X - Achse")
    plt.ylabel("Y - Achse")
    plt.show()

def aufgabe2():
    random_arrayx = np.random.rand(5)  # массив из 5 случайных чисел
    random_arrayy = np.random.rand(5)  # массив из 5 случайных чисел

    plt.scatter(random_arrayx, random_arrayy)
    plt.title("диаграмма рассеяния для двух наборов случайных данных")
    plt.xlabel("X - Achse")
    plt.ylabel("Y - Achse")
    plt.show()
