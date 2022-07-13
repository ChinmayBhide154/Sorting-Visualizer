import matplotlib.pyplot as plt
import numpy as np
from Sorter import Sorter

num_values = 15
lst = np.random.randint(0, 100, num_values)
x = np.arange(0, num_values, 1)

sorter = Sorter(lst, x, num_values, 100, 0, 0.01)
sorter.bubble_sort()
