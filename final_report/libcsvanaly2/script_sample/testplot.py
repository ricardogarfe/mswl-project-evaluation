import numpy as np
import matplotlib.pyplot as plt

class Pendulum:

    def __init__(self):
        self.fig = plt.figure()

    def plot1(self):
        ax = self.fig.add_subplot(211)
        ax.plot([1,2],[3,4])

    def plot2(self):
        ax = self.fig.add_subplot(212)
        ax.plot([1,2],[4,3])

p = Pendulum()
p.plot1()
p.plot2()
plt.show()
