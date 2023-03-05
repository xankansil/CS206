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


class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)

        self.robot = robot.ROBOT()
        self.world = world.WORLD()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for x in range(c.program_run_time):
            p.stepSimulation()
            time.sleep(c.sleep_time)
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act()
