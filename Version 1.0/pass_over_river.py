from game import *

action = ["moveLeft", "moveRight", "get", "push"]

class PassOverRiver2_3(GameState):
    def __init__(self, prevState = None):
        self.left = []
        self.right = ["sheep", "wolf", "cabbage"]
        self.boat = ["farmer"]
        self.pos = 1
        self.state = StatePassOverRiver2_3(self.left, self.right, self.boat, self.pos)

    def run(self):
        while not self.isGoalState():
            self.print(self.state)
            for i in range (len(action)):
                print(str(action[i]) + ' ' + str(i))
            choice = int(input())
            self.changeState(self.state, action[choice])
            if not self.state.check():
                print("you lose")
                break;
            if choice == -1:
                break
            if self.isGoalState():
                print("this is goal state")
        print("end game")


    def changeState(self, prevState = None, action = None):
        if action == "moveLeft":
            if prevState.pos == 1:
                prevState.pos = -1
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
            elif prevState.pos == -1:
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
        elif action == "moveRight":
            if prevState.pos == -1:
                prevState.pos = 1
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
            elif prevState.pos == 1:
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
        elif action == "get":
            if prevState.pos == 1:
                for e in prevState.right:
                    print(e)
                choice = input()
                prevState.right.remove(choice)
                prevState.boat.append(choice)
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
            elif prevState.pos == -1:
                for e in prevState.left:
                    print(e)
                choice = input()
                prevState.left.remove(choice)
                prevState.boat.append(choice)
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
        elif action == "push":
            if prevState.pos == 1:
                for e in prevState.boat:
                    print(e)
                choice = input()
                prevState.boat.remove(choice)
                prevState.right.append(choice)
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState
            elif prevState.pos == -1:
                for e in prevState.boat:
                    print(e)
                choice = input()
                prevState.boat.remove(choice)
                prevState.left.append(choice)
                newState = StatePassOverRiver2_3(prevState.left, prevState.right, prevState.boat, prevState.pos)
                self.state = newState

    def startState(self, state):
        left = []
        right = ["sheep", "wolf", "cabbage"]
        boat = ["farmer"]
        pos = 1
        state = StatePassOverRiver2_3(left, right, boat, pos)
        return state

    def isGoalState(self):
        if len(self.left) + len(self.boat) == 4:
            return True
        return False

    def getNeighbourhood(self, current):
        pass

    def print(self, state):
        print('\n')
        print("state current")
        print("left " + str(state.left) + ' ' * 10 + "right" + str(state.right))
        if state.pos == -1:
            print("boat" + str(state.boat) + "in left")
        elif state.pos == 1:
            print("boat" + str(state.boat) + "in right")
        print()

class StatePassOverRiver2_3:

    def __init__(self, left , right, boat, pos):
        self.agent = {"sheep", "wolf", "cabbage", "farmer"}
        self.left = left
        self.right = right
        self.boat = boat
        self.pos = pos

    def check(self):
        agents = self.left + self.boat + self.right
        if self.pos == 1:
            if ("cabbage" in self.left and "sheep" in self.left) or ("wolf" in self.left and "sheep" in self.left):
                return False
        else:
            if ("cabbage" in self.right and "sheep" in self.right) or ("wolf" in self.right and "sheep" in self.right):
                return False
        data = set(agents)
        if data == self.agent:
            return True
        return False




