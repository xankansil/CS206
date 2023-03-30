import pyrosim.pyrosim as pyrosim
import random

pyrosim.Start_SDF("world.sdf")

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    
    x = 3
    y = 3
    z = 3

    length = 1
    width = 1
    height = 1

    #pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    #backleg
    pyrosim.Send_Cube(name="Link0", pos=[0.5, 0.5, 0.5], size=[length, width, height])
    #joint torso_backleg
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[1.0, 0.5, 1.0])
    #torso
    pyrosim.Send_Cube(name="Link1", pos=[0.5, 0.0, 0.5], size=[length, width, height])
    #joint torso_frontleg
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[1.0, 0.0, 0.0])
    #frontleg
    pyrosim.Send_Cube(name="Link2", pos=[0.5, 0.0, -0.5], size=[length, width, height])
    
    pyrosim.End()
    
def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    #sensor neurons
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Link1")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = 'Link0')
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = 'Link2')
    #motor neurons
    pyrosim.Send_Motor_Neuron(name = 3 , jointName = 'Link0_Link1')
    pyrosim.Send_Motor_Neuron(name = 4 , jointName = 'Link1_Link2')
    #synapses

    for sensorneuron in range(3):
        for motorneuron in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName=sensorneuron, targetNeuronName=motorneuron,weight=random.randrange(-1, 1))

            
##    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1)
##    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1)
##    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=1)
##    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=-1)

    
    pyrosim.End()

    
Create_World()
Generate_Body()
Generate_Brain()

















