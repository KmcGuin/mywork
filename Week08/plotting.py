#plotting.py
#Author: Kealan McGuinness
# Write a program that plots the function y = x2.

import matplotlib.pyplot as plt
import numpy as np

x_points = np.array(range(1,101))
y_points = x_points * x_points

plt.plot (x_points, y_points)
plt.show()

