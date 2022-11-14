from node import Node
from time import process_time


class CostAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.marioPos = self.firstNode.searchForMario()
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getNodeMinCost(self, stack):
        minNode = min(stack, key=lambda node: node.getCost())
        return minNode

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def start(self):
        startTime = process_time()

        stack = self.stack
        marioPos = self.marioPos
        # marioPos0 = self.marioPos0
        currentNode = stack[0]
        expandedNodes = 0
        depth = 0
        starts = currentNode.searchForStart()
        start1 = starts[0]
        start2 = starts[1]
        flowers = currentNode.searchForFlower()
        flower1 = flowers[0]
        flower2 = flowers[1]
        while not (currentNode.isGoal()):
            # Check if right side is free
            # if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1 and currentNode.getFather().getOperator() != "left"):
            print("---")
            print(currentNode.getMarioPos())
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                # if (currentNode.avoidGoBack("right", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.rightMovement(marioPos))
                son.moveRight(marioPos)
                if (son.avoidGoBack2("right", start1, start2, flower1, flower2)):
                    stack.append(son)

                    print("El costo actual es: " + str(son.getCost()))
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if left side is free
            # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
               # if (currentNode.avoidGoBack("left", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.leftMovement(marioPos))
                son.moveLeft(marioPos)
                if (son.avoidGoBack2("left", start1, start2, flower1, flower2)):
                    stack.append(son)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    
                    print(son.getMarioPos())

            # Check if down side is free
            # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
               # if (currentNode.avoidGoBack("down", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.downMovement(marioPos))
                son.moveDown(marioPos)
                if (son.avoidGoBack2("down", start1, start2, flower1, flower2)):
                    stack.append(son)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                        
                    print(son.getMarioPos())

            # Check if up side is free
            # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
               # if (currentNode.avoidGoBack("up", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.upMovement(marioPos))
                son.moveUp(marioPos)
                if (son.avoidGoBack2("up", start1, start2, flower1, flower2)):
                    stack.append(son)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())
            # stack.pop(0)
            # currentNode = stack[0]
            stack.remove(currentNode)

            currentNode = self.getNodeMinCost(stack)
            expandedNodes += 1
            print("costo actual: " + str(currentNode.getCost()))
            starts = currentNode.searchForStart()
            start1 = starts[0]
            start2 = starts[1]
            flowers = currentNode.searchForFlower()
            flower1 = flowers[0]
            flower2 = flowers[1]
            print("flower", flower1, flower2)
            marioPos = currentNode.searchForMario()

        # print(currentNode.getFather().getDepth())
        # print(currentNode.getState())
        # print(currentNode.recreateSolution())

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        print("El costo final de la solución es: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("expandido", expandedNodes+1)  # Good
        print("profundidad", depth)
        return [solutionWorld, expandedNodes+1, depth]
