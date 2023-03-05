import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
##    def __init__(self, jointName) -> None:
##        self.jointName = jointName
##        self.Prepare_To_Act()
##
##    def Prepare_To_Act(self):
##        self.amplitude = c.amplitudeBackLeg
##        self.offset = c.phaseOffsetBackLeg
##
##        if (self.jointName == 'Link0_Link1'):
##            self.frequency = c.frequencyBackLeg
##        else:
##            self.frequency = c.frequencyBackLeg / 2
##
##        val = self.frequency * numpy.linspace(0, 2 * c.pi, c.program_run_time) + self.offset
##        self.motorValues = self.amplitude * numpy.sin(val)
##
##    def Set_Value(self, t, robot):
##        pyrosim.Set_Motor_For_Joint(bodyIndex=robot.robotId,
##                                    jointName=self.jointName,
##                                    controlMode=p.POSITION_CONTROL,
##                                    targetPosition=self.motorValues[t],
##                                    maxForce=100)

    def Set_Values(self, robotId, desiredAngle):
        self.robotId = robotId

        if(self.jointName == "Link1_Link2"):
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robotId,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=desiredAngle,
                maxForce=c.maxForce)
        else:
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robotId,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=-desiredAngle,
                maxForce=c.maxForce)

            
        

