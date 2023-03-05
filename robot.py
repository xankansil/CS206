from ntpath import join
import numpy
import pybullet as p
from motor import MOTOR
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                #self.motors[jointName].Set_Values(self.robotId, desiredAngle)
                for i in self.motors: 
                    for i in self.motors: 
                        self.motors[i].Set_Values(self.robotId, desiredAngle)
                print(neuronName, jointName, desiredAngle)


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self, timeStep):
        self.timeStep = timeStep
        for i in self.sensors:
            self.sensor = self.sensors[i]
            self.sensor.Get_Value(self.timeStep)

    def Think(self):
        self.nn.Update()
        self.nn.Print()


