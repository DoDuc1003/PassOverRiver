from abc import *


class GameState:
    """

    """
    @abstractmethod
    def __init__(self, prevState = None):
        pass

    @abstractmethod
    def changeState(self, prevState=None, action = None):
        pass

    @abstractmethod
    def startState(self, state):
        pass

    @abstractmethod
    def isGoalState(self):
        pass

    @abstractmethod
    def getNeighbourhood(self, current):
        pass

class Agent:
    def __init__(self, name, index = -1):
        self.name = name
        self.__index = index

    def getAction(self, state):
        pass

    def getIndex(self):
        pass

class GameRule:
    pass


