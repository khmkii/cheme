import matplotlib.pyplot as plt


class SimpleMultipleContactExtraction:
    def __init__(self, x_array, y_array):
        self.x_array = x_array
        self.y_array = y_array

    def equilibrium_curve(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(self.x_array, self.y_array, 'k')
        plt.show()
