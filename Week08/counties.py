# counties.py
# Author: Kealan McGuinness
# Write program that has a list of counties, make it a long list (pick from five
#counties). Make some counties appear more than others. Make a pie chart of the
# counties.

import numpy as np
import matplotlib.pyplot as plt

possible_counties = ['mayo','donegal','cork','tipperary']

counties = np.random.choice(
        possible_counties,
        p=[0.1, 0.3, 0.2, 0.12, 0.28 ],
        size=(100)
)

unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels= unique)
plt.bar(unique, counts)
plt.show()