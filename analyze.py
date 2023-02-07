import numpy as numpy
import matplotlib.pyplot as matplotlib

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

matplotlib.plot(backLegSensorValues, label = "Link0", linewidth = 4)
matplotlib.plot(frontLegSensorValues, label = "Link2")

matplotlib.legend()
matplotlib.show()
