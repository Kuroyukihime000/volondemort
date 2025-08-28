import math
import matplotlib.pyplot as plt
import numpy as np
import math

def area_circle():
    r = float(input("Введите радиус круга: "))
    print(f"Площадь круга: {math.pi * r ** 2:.2f}")

def area_rectangle():
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))
    print(f"Площадь прямоугольника: {a * b:.2f}")

def area_triangle():
    base = float(input("Введите основание: "))
    height = float(input("Введите высоту: "))
    print(f"Площадь треугольника: {0.5 * base * height:.2f}")

def compute_log():
    x = float(input("Введите число: "))
    base = input("Введите основание логарифма (по умолчанию e): ").strip()
    if base == "":
        print(f"ln({x}) = {math.log(x):.4f}")
    else:
        b = float(base)
        print(f"log_{b}({x}) = {math.log(x, b):.4f}")

def compute_factorial():
    n = int(input("Введите целое число: "))
    print(f"{n}! = {math.factorial(n)}")


def plot_function():
    expr = input("Введите выражение от x (например: x**2 - 3*x + 2): ")
    x = np.linspace(-10, 10, 400)
    try:
        y = eval(expr, {"x": x, "math": math, "np": np})
        plt.plot(x, y)
        plt.title(f"График функции: {expr}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Ошибка при построении графика: {e}")
