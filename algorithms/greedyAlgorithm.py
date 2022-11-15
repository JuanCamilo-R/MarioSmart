from node import Node
from time import process_time


class GreedyAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.marioPos = self.firstNode.searchForMario()
        self.princessPos = self.searchForPrincess(world)
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getNodeMinHeuristic(self, stack):
        minNode = min(stack, key=lambda node: node.getHeuristic())
        return minNode

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def searchForPrincess(self, world):
        princessPos = []
        for i in range(10):
            for j in range(10):
                if (world[i, j] == self.firstNode.PRINCESS):
                    princessPos.append(i)
                    princessPos.append(j)
        return princessPos

    def start(self):
        startTime = process_time()

        stack = self.stack
        marioPos = self.marioPos
        currentNode = stack[0]
        expandedNodes = 0
        depth = 0
        
        while not (currentNode.isGoal()):
            # Check if right side is free
            print("---")
            print(currentNode.getMarioPos())
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                right = son.rightMovement(marioPos)

                if (son.compareCicles2(right)):
                    son.setNewCost(right)
                    son.setMarioPos(right)
                    sonManhattanDistance = son.calculateManhattanDistance(self.princessPos)
                    sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                    son.setHeuristic(sonHeuristic)
                    stack.append(son)

                    son.moveRight(marioPos)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if left side is free
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                left = son.leftMovement(marioPos)

                if (son.compareCicles2(left)):
                    son.setNewCost(left)
                    son.setMarioPos(left)
                    sonManhattanDistance = son.calculateManhattanDistance(self.princessPos)
                    sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                    son.setHeuristic(sonHeuristic)
                    stack.append(son)

                    son.moveLeft(marioPos)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if down side is free
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                
                down = son.downMovement(marioPos)

                if (son.compareCicles2(down)):
                    son.setNewCost(down)
                    son.setMarioPos(down)
                    sonManhattanDistance = son.calculateManhattanDistance(self.princessPos)
                    sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                    son.setHeuristic(sonHeuristic)
                    stack.append(son)

                    son.moveDown(marioPos)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if up side is free
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                
                up = son.upMovement(marioPos)

                if (son.compareCicles2(up)):
                    son.setNewCost(up)
                    son.setMarioPos(up)
                    sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                    sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                    son.setHeuristic(sonHeuristic)
                    stack.append(son)

                    son.moveUp(marioPos)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            stack.remove(currentNode)

            currentNode = self.getNodeMinHeuristic(stack)
            expandedNodes += 1
            marioPos = currentNode.getMarioPos()
            print("Mario pos:", marioPos)

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        print("Heurística meta: ", currentNode.getHeuristic())
        print(currentNode.recreateSolution())
        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("expandido", expandedNodes+1)  # Good
        print("profundidad", depth)
        print("El costo final de la solución es: " + str(currentNode.getCost()))
        return [solutionWorld, expandedNodes+1, depth]
