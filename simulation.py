import pybullet as p
from robot import ROBOT
from world import WORLD
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
from cmath import pi
import random
import math
import constants as c
import world
import robot
import time as t


class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)

        self.robot = robot.ROBOT()
        self.world = world.WORLD()


    def Run(self):
        for x in range(c.SIMULATION_STEPS):
            p.stepSimulation()
            ROBOT.Sense(self.robot)
            ROBOT.Think(self.robot)
            ROBOT.Act(self.robot)
            
            t.sleep(c.sleep_time)

    def __del__():
        p.disconnect()
