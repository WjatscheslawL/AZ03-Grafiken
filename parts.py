import matplotlib.pyplot as plt


def part1():
    x = [2, 6, 8, 14, 7]
    y = [6, 4, 10, 12, 9]
    plt.plot(x, y)
    plt.title("Beispiel einfache lineale")
    plt.xlabel("X - Achse")
    plt.ylabel("Y - Achse")
    plt.show()


def histogram():
    data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]
    plt.hist(data, bins=6)
    plt.title("Beispiel:  einfache Histofgram")
    plt.xlabel("X - Achse")
    plt.ylabel("Y - Achse")
    plt.show()


def verteilung():
    x = [2, 6, 8, 14, 7]
    y = [6, 4, 10, 12, 9]
    plt.scatter(x, y)
    plt.title("Beispiel: Verteilung")
    plt.xlabel("X - Achse")
    plt.ylabel("Y - Achse")
    plt.show()
