import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for x in range(100):
	p.stepSimulation()
	time.sleep(1/60)
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link0")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
	print(x)
	
p.disconnect()

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
