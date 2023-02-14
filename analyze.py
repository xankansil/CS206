import numpy as numpy
import matplotlib.pyplot as matplotlib

#matplotlib.plot(backLegSensorValues, label = "Link0", linewidth = 4)
#matplotlib.plot(frontLegSensorValues, label = "Link2")


backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
backLegJointValues = numpy.load("data/backLegJointValues.npy")
frontLegJointValues = numpy.load("data/frontLegJointValues.npy")

matplotlib.plot(backLegJointValues, linewidth=2, label='BackLeg')
matplotlib.plot(frontLegJointValues, linewidth=2, label='FrontLeg')

matplotlib.legend()
matplotlib.show()
