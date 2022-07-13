import matplotlib.pyplot as plt

class Sorter:
    def __init__(self, list_values, arranged_values, num_values, max_value, min_value, pause_time):
        self.list_values = list_values
        self.arranged_values = arranged_values
        self.num_values = num_values
        self.max_value = max_value
        self.min_value = min_value
        self.pause_time = pause_time

    def bubble_sort(self):
        for i in range(self.num_values):
            for j in range(self.num_values - i - 1):
                plt.bar(self.arranged_values, self.list_values)
                plt.pause(self.pause_time)
                plt.clf()

                if self.list_values[j] > self.list_values[j + 1]:
                    self.list_values[j], self.list_values[j + 1] = self.list_values[j + 1], self.list_values[j]

        plt.show()