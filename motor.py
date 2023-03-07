import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.offset = 0
        self.frequency = 0
        self.amplitude = 0
        self.motorValues = numpy.zeros(c.SIMULATION_STEPS)



    def Set_Values(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex=robot,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=desiredAngle,
                maxForce=c.maxForce)

            
        

