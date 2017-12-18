# -*- coding: utf-8 -*-
"""

Created on Oct 31 13:44:33 2017

@author: ed12k3b

Programming for Geographical Information Analysts: Core Skills
Module taught for MA Social Research Methods (Interdisciplinary)
Module taught by Dr. Andy Evans, University of Leeds.

This file contains the code for the Agent class.

"""

# Import the modules required for model creation

import random


# Defining the class for the agents within the environment

class Agent ():
    def __init__(self, environment, agents, neighbourhood, y, x):
        self.x = random.randint (0,len(environment))
        self.y = random.randint (0,len(environment))
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        self.environment = environment
        self.agents = agents
        self.store = 0 
        self.neighbourhood = neighbourhood

        
# Moving the agents in the environment; division % constrains the agents within the environment's perimeter. If one or more of the agents are found 
# out of range, it will arrive on the parralel side
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)

        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)
            
            
# Agents eat a patch in the position they were stood, but when they move, they also lose one store
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
            
# The agents can now eat what is leftover in that position within the environment (if the number is under ten), adding to their stores
        
        elif self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -=10
            self.store +=10
            
            
# If an agent reaches a store capacity of >1000, the agent will vomit 1000 of its stores where it is stood

    def vomit(self):
        if self.store >=1000:
            self.environment[self.y][self.x] +=1000
            self.store = self.store-1000

            
# Agents have neighbours which they share their food stores with if they are near them. If they fall within a distance of a neighbourhood, 
# change both the agent and its neighbour's store to an average number
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
               #print("sharing " + str(dist) + " " + str(ave)) # code to test and view agent store changes
                

# Pythagoras code for calculating distance between the two agent coordinates
                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    