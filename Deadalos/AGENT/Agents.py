
"""
AGENT STATES:

ALIVE
AT RISK
DEAD
MULTIPLY
"""


class Agent(object):
    
    def __init__(self,ID):
        self.ID = str(ID)
        self.state = "ALIVE"
    
    def changeState(self,newState):
        self.state = str(newState)

class Bacterium(Agent):
    
    def __init__(self,ID,oxygen,food,multiply):
        self.ID = str(ID)
        self.oxygen = int(oxygen)
        self.food = int(food)
        self.multiply = int(multiply)
        self.state = "ALIVE"

class Plant(Agent):
    
    def __init__(self,ID,oxygen,food,multiply):
        self.ID = str(ID)
        self.oxygen = int(oxygen)
        self.food = int(food)
        self.multiply = int(multiply)
        self.state = "ALIVE"

class Human(Agent):
    
    def __init__(self,ID,gender,oxygen,food,multiply):
        self.ID = str(ID)
        self.gender = str(gender)
        self.oxygen = int(oxygen)
        self.food = int(food)
        self.multiply = int(multiply)
        self.state = "ALIVE"