#ages.py
#Author: Kealan McGuinness
# Write a program that makes a list called ages that has, the same number random
# values as salaries, (range:21 to 65) . Make scatter plot of this data.

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint (low=21, high=65, size =number_of_entries)

plt.scatter(ages, salaries)
x_points = np.array(range(1, 101))
y_points = x_points * x_points 

plt.plot(x_points, y_points, color = 'red', label='x squared')

plt.title('random plot')
plt.xlabel('salaries')
plt.ylabel('age')
plt.legend()
plt.savefig('prettier-plot.png')
plt.show()