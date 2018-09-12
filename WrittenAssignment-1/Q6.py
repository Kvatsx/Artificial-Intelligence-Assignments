# Kaustav Vats (2016048)
# Algorithm will return No Match if not found.
# else will return a Match found

# How to run this file?
# In Terminal Type: python3 Q6.py

import queue as Q
from time import time

class Node:

    def __init__(self, key1, key2, steps, link):
        self.UID = str(key1) + str(key2)
        self.key1 = key1
        self.key2 = key2
        self.steps = steps
        self.distance = 0
        self.link = link

    def isEqual(self, size):
        return self.UID == str(size-1) + str(size-1)

    def __lt__(self, other):
        return self.steps < other.steps

    def __eq__(self, other):
        return self.steps == other.steps

class Transport:

    def __init__(self, size):
        self.size = size

    # This method finds all node and update their F cost function.
    def findAllNodes(self, node, size):
        Children = []

        if ( node.key1+1 < size and node.key2+1 < size ):
            flag = True
            if ( node.key1+1 == size-1 and node.key2+1 != size-1 ):
                flag = False
            if ( node.key1+1 != size-1 and node.key2+1 == size-1 ):
                flag = False
            if ( flag ):
                n1 = Node(node.key1+1, node.key2+1, node.steps+1, None)
                dist = self.calculateHeuristicDistance(n1, size)
                n1.distance = dist + node.steps
                Children.append(n1)

        if ( node.key1+1 < size and node.key2+4 < size ):
            flag = True
            if ( node.key1+1 == size-1 and node.key2+4 != size-1 ):
                flag = False
            if ( node.key1+1 != size-1 and node.key2+4 == size-1 ):
                flag = False
            if ( flag ):
                n1 = Node(node.key1+1, node.key2+4, node.steps+1, None)
                dist = self.calculateHeuristicDistance(n1, size)
                n1.distance = dist + node.steps
                Children.append(n1)

        if ( node.key1+4 < size and node.key2+1 < size ):
            flag = True
            if ( node.key1+4 == size-1 and node.key2+1 != size-1 ):
                flag = False
            if ( node.key1+4 != size-1 and node.key2+1 == size-1 ):
                flag = False
            if ( flag ):
                n1 = Node(node.key1+4, node.key2+1, node.steps+1, None)
                dist = self.calculateHeuristicDistance(n1, size)
                n1.distance = dist + node.steps
                Children.append(n1)

        if ( node.key1+4 < size and node.key2+4 < size ):
            flag = True
            if ( node.key1+4 == size-1 and node.key2+4 != size-1 ):
                flag = False
            if ( node.key1+4 != size-1 and node.key2+4 == size-1 ):
                flag = False
            if ( flag ):
                n1 = Node(node.key1+4, node.key2+4, node.steps+1, None)
                dist = self.calculateHeuristicDistance(n1, size)
                n1.distance = dist + n1.steps
                Children.append(n1)

        return Children

    def calculateHeuristicDistance(self, node, size):
        size = size-1
        a = size - node.key1
        b = size - node.key2
        # avg = (a + b)/2
        avg = min(a, b) + abs(node.key1 - node.key2)
        return avg

    def aStarAlgorithm(self, root, end):
        visited = {}
        q = Q.PriorityQueue()
        dist = self.calculateHeuristicDistance(root, end)
        root.distance = dist
        q.put((1, root))
        visited[root.UID] = root
        Count = 0

        while ( not q.empty() ):
            Count += 1
            current_Node = (q.get())[1]
            # print(current_Node.key1, current_Node.key2, " currentNode:Dist: ", current_Node.distance)
            if ( current_Node.isEqual(end) ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.steps)
                return True
            
            Neighbours = self.findAllNodes(current_Node, end)
            current_Node.link = Neighbours
            # for i in range(len(Neighbours)):
            #     print(Neighbours[i].key1, Neighbours[i].key2, " Distance: ", Neighbours[i].distance)
            # print("Children Done\n")

            for i in range(len(Neighbours)):
                if ( Neighbours[i].UID not in visited ):
                    q.put((Neighbours[i].distance, Neighbours[i]))
                    visited[Neighbours[i].UID] = Neighbours[i]

        return False

    def bfs(self, root, end):
        visited = {}
        queue = []
        queue.append(root)
        visited[root.UID] = root
        Count = 0
        while ( True ):
            Count += 1
            if ( len(queue) == 0 ):
                return False
            current_Node = queue.pop(0)
            # print(current_Node.key1, current_Node.key2, " currentNode:Dist: ", current_Node.distance, "\n")

            if ( current_Node.isEqual(end) ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.steps)
                return True
            Neighbours = self.findAllNodes(current_Node, end)
            current_Node.link = Neighbours

            # for i in range(len(Neighbours)):
                # print(Neighbours[i].key1, " ", Neighbours[i].key2, " Distance: ", Neighbours[i].distance)
            # print("Children Done\n")

            for i in range(len(Neighbours)):
                if Neighbours[i].UID not in visited:
                    # Neighbours[i].step = current_Node.step + 1
                    queue.append(Neighbours[i])
                    visited[Neighbours[i].UID] = Neighbours[i]      
                
if __name__ == "__main__":

    N = 50
    tp = Transport(N)
    Root = Node(0, 30, 0, None)

    t1 = int(round(time()*1000))
    if ( tp.bfs(Root, N) ):
        print("Found Match BFS")
    else:
        print("No Match BFS")
    t2 = int(round(time()*1000))
    print("Total time taken by Bfs: ", t2-t1)
    print("")

    t1 = int(round(time()*1000))
    if ( tp.aStarAlgorithm(Root, N) ):
        print("Found Match A*")
    else:
        print("No Match A*")
    t2 = int(round(time()*1000))
    print("Total time taken by A*: ", t2-t1)
    print("")