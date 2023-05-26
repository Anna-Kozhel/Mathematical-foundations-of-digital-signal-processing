import statistics
import numpy as math
import matplotlib.pyplot as plot
from colorama import Style, Fore


def arithmeticMean(values): return math.mean(values)


def harmonicMean(values): return len(values) / math.sum(1 / math.abs(values))


def geometricMean(values):
    specificValues = [(value if value >= 0 else math.abs(value)) for value in values]
    return statistics.geometric_mean(specificValues)


def errorCalculating(approximate, accurate):
    absolute, relative = math.abs(approximate - accurate), math.abs(approximate - accurate) / math.abs(accurate) * 100
    return math.max(absolute), math.min(absolute), math.max(relative), math.min(relative)


def printGraphic(x, approximate, accurate):
    plot.title("N = " + str(N))
    plot.plot(x, [approximateArithmetic] * len(x), label='- середнє арифметичне', color="#C3B5A9")
    plot.plot(x, [approximateGeometric] * len(x), label='- середнє гармонічне', color="#9C8570")
    plot.plot(x, [approximateHarmonic] * len(x), label='- середнє геометричне', color="#5D4F43")
    plot.plot(x, approximate, label='- наближена функція', color=(0.9647, 0.6784, 0.0235))
    plot.plot(x, accurate, label='- точна функція', color="#1fadff", linewidth=2)
    plot.xlabel('x')
    plot.ylabel('y')
    plot.legend()
    plot.show()


def printMessage():
    for i in range(3):
        print("Наближене середнє " + names[i] + "е:\t" + Style.BRIGHT + Fore.YELLOW + str(dataMeans[i][0]) + Style.RESET_ALL)
        print("Точне середнє " + names[i] + "е:\t\t" + Style.BRIGHT + Fore.YELLOW + str(dataMeans[i][1]) + Style.RESET_ALL, end="\n\n")


n = 10
N, A, phi, error = 1000 * n, 1.0, math.pi / 4, 0.05
x = math.linspace(0, 0.5, N)
noise = math.random.uniform(-error * A, error * A, N)
yApproximate, yAccurate = A * math.sin(n * x + phi) + noise + n, A * math.sin(n * x + phi) + n
names = ["арифметичн", "гармонічн", "геометричн"]
dataMeans = []

approximateArithmetic, accurateArithmetic = arithmeticMean(yApproximate), arithmeticMean(yAccurate)
dataMeans.append([approximateArithmetic, accurateArithmetic])

approximateHarmonic, accurateHarmonic = harmonicMean(yApproximate), harmonicMean(yAccurate)
dataMeans.append([approximateHarmonic, accurateHarmonic])

approximateGeometric, accurateGeometric = geometricMean(yApproximate), geometricMean(yAccurate)
dataMeans.append([approximateGeometric, accurateGeometric])

maxAbsolute, minAbsolute, maxRelative, minRelative = errorCalculating(yApproximate, yAccurate)

printGraphic(x, yApproximate, yAccurate)
printMessage()

print("Абсолютна максимальна похибка:\t" + Style.BRIGHT + Fore.CYAN + str(maxAbsolute) + Style.RESET_ALL)
print("Абсолютна мінімальна похибка:\t" + Style.BRIGHT + Fore.CYAN + str(minAbsolute) + Style.RESET_ALL)
print("Відносна максимальна похибка:\t" + Style.BRIGHT + Fore.CYAN + str(maxRelative) + Style.RESET_ALL)
print("Відносна мінімальна похибка:\t" + Style.BRIGHT + Fore.CYAN + str(minRelative) + Style.RESET_ALL)
