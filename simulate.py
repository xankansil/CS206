import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
from cmath import pi
import random
import math


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

length = 1000

backLegSensorValues = numpy.zeros(length)
frontLegSensorValues = numpy.zeros(length)

backLegJointValues = numpy.zeros(length)
frontLegJointValues = numpy.zeros(length)

amplitudeBackLeg = math.pi/4.0
frequencyBackLeg = 1/20.0
phaseOffsetBackLeg = 0

amplitudeFrontLeg = -math.pi/4.0
frequencyFrontLeg = 1/10.0
phaseOffsetFrontLeg = math.pi/8


for x in range(length):
	p.stepSimulation()
	time.sleep(1/60)
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link0")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
	print(x)

	backLegPosition = math.sin(frequencyBackLeg * x + phaseOffsetBackLeg) * amplitudeBackLeg
	frontLegPosition = math.sin(frequencyFrontLeg * x + phaseOffsetFrontLeg) * amplitudeFrontLeg

	backLegJointValues[x] = backLegPosition
	frontLegJointValues[x] = frontLegPosition
    
	pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName= 'Link0_Link1',
        controlMode=p.POSITION_CONTROL,
        targetPosition= backLegPosition,
        maxForce=100)

	pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName= 'Link1_Link2',
        controlMode=p.POSITION_CONTROL,
        targetPosition= frontLegPosition,
        maxForce=100)
	
p.disconnect()

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

numpy.save("data/backLegJointValues.npy", backLegJointValues)
numpy.save("data/frontLegJointValues.npy", frontLegJointValues)



