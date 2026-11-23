# 1. Quadratic Calculator and Grapher
# Simple project I wanted to make to see if in a short span of time, I can create a simple calculator that can present
# 2D equations and plot them.
import numpy as np
import matplotlib.pyplot as plt

x_squared = float(input("What is the value of x^2? "))
x = float(input("What is the value of x? "))
c = float(input("What is the value of c? "))

print(f"The quadratic equation is: {x_squared}x^2 + {x}x + {c} = 0")

rangeX = np.linspace(-25, 25, 1000)
rangeY = x_squared * rangeX**2 + x * rangeX + c

plt.title("Quadratic Equation Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.plot(rangeX, rangeY)
plt.show()