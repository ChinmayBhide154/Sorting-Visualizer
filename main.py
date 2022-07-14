import matplotlib.pyplot as plt
import numpy as np
from Sorter import Sorter


num_values = 15
values = np.random.randint(0, 100, num_values)
x = np.arange(0, num_values, 1)

sorter = Sorter(values, x, num_values, 100, 0, 0.01)
sorter.insertion_sort()
sorter.bubble_sort()
