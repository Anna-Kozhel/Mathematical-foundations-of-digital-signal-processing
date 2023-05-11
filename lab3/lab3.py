import numpy as math
import matplotlib.pyplot as plot
import time

amountSum, amountMultiplication = 0, 0


def function():
    return math.random.uniform(-1, 1)


def fastFourierTransform(f):
    global amountSum, amountMultiplication
    n = len(f)
    if n == 1:
        return f
    else:
        even, odd = fastFourierTransform(f[::2]), fastFourierTransform(f[1::2])
        factor = math.exp(-2j * math.pi * math.arange(n) / n)
        amountSum += 2
        amountMultiplication += 4
        return math.concatenate([even + factor[:n // 2] * odd, even + factor[n // 2:] * odd])


def printMessage():
    print("\n   ", "\b——————" * 10, "\n",
          "  |  k   |                    c_k                    |")
    print("   ", "\b——————" * 10, "")
    for i in range(N):
        print("   | {:<5}|   {:<39.15f} |".format(i, C_ks[i]))
    print("   ", "\b——————" * 10, "\n")

    print(f"\tШПФ:\nN: 2^{P} = {N}")
    print("Час обчислення:", time)
    print("Кількість операцій додавання:", amountSum)
    print("Кількість операцій множення:", amountMultiplication)


def printGraphic():
    graph1, ax1 = plot.subplots(figsize=(10, 10))
    ax1.set_title('Графік спектру амплітуд', fontsize=18)
    plot.grid(True)
    for i in range(N):
        plot.plot(i, amplitudeSpectrum[i], linewidth=4)
        plot.plot([i, i], [0, amplitudeSpectrum[i]], linewidth=4)
    plot.xlabel('k')
    plot.ylabel('|C_k|')
    plot.show()

    graph2, ax2 = plot.subplots(figsize=(10, 10))
    ax2.set_title('Графік спектру фаз', fontsize=18)
    plot.grid(True)
    for i in range(N - 1):
        plot.plot(i, phaseSpectrum[i], linewidth=4)
        plot.plot([i, i], [0, phaseSpectrum[i]], linewidth=4)
    plot.xlabel('k')
    plot.ylabel('arg(C_k)')
    plot.show()


P = 10
N = 2 ** P
func = [function() for _ in range(N)]
start = time.time()
C_ks = fastFourierTransform(func)
time = time.time() - start
printMessage()
amplitudeSpectrum, phaseSpectrum = [], []
for k in range(N):
    amplitudeSpectrum.append(abs(C_ks[k]))
    phaseSpectrum.append(math.angle(C_ks[k]))
printGraphic()
