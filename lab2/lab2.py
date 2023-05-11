import numpy as math
import matplotlib.pyplot as plot
import time


def function():
    return math.random.uniform(-1, 1)


def coefficientAkCalculating(k, n, a_k=0):
    for i in range(n): a_k += (1 / n) * function() * math.cos((2 * math.pi * k * i) / n)
    return a_k


def coefficientBkCalculating(k, n, b_k=0):
    for i in range(n): b_k += (-1 / n) * function() * math.sin((2 * math.pi * k * i) / n)
    return b_k


def FourierCoefficients(n):
    a_ks, b_ks, c_ks = [], [], []
    sumAmount, multiplicationAmount, start = 0, 0, time.time()
    for i in range(n):
        a_k, b_k = coefficientAkCalculating(i, n), coefficientBkCalculating(i, n)
        a_ks.append(a_k)
        b_ks.append(b_k)
        c_ks.append(a_k + 1j * b_k)
        sumAmount += 2 * n
        multiplicationAmount += 8 * n + 2
    end = time.time()
    return a_ks, b_ks, c_ks, sumAmount, multiplicationAmount, end - start


def printMessage():
    print("\n   ", "\b—————" * 25, "\b\b\n",
          "  | k  |           a_k          |           b_k          |                     c_k                   |")
    print("   ", "\b—————" * 25, "\b\b")
    for i in range(0, N):
        print("   | {:<3}|   {:<20.15f} |   {:<20.15f} |   {:<39.15f} |".format(i, A_ks[i], B_ks[i], C_ks[i]))
    print("   ", "\b—————" * 25, "\b\b\n")
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
        plot.plot([i, i], [0, phaseSpectrum[i]],linewidth=4)
    plot.xlabel('k')
    plot.ylabel('arg(C_k)')
    plot.show()


N = 20
A_ks, B_ks, C_ks, amountSum, amountMultiplication, time = FourierCoefficients(N)
amplitudeSpectrum, phaseSpectrum = [math.sqrt(A_ks[k] ** 2 + B_ks[k] ** 2) for k in range(N)], [math.angle(C_ks[k])for k in range(N)]
printMessage()
printGraphic()
