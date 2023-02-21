import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p


class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.offset = c.phaseOffsetBackLeg

        if (self.jointName == 'Link0_Link1'):
            self.frequency = c.frequencyBackLeg
        else:
            self.frequency = c.frequencyBackLeg / 2

        val = self.frequency * numpy.linspace(0, 2 * c.pi, c.program_run_time) + self.offset
        self.motorValues = self.amplitude * numpy.sin(val)

    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot.robotId,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=self.motorValues[t],
                                    maxForce=100)

    def Save_Values(self):
        numpy.save('data\\MotorValues.npy', self.motorValues)

