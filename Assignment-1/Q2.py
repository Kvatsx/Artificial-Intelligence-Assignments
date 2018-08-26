#!/usr/bin/python
# Kaustav Vats (2016048)

from time import time
import queue as Q

class Node:
    
    def __init__(self, node, step, GraphNode, Link):
        self.UID = ""
        self.step = step
        self.node = node
        self.distance_top = 0
        self.distance = 0
        self.GraphNode = GraphNode
        self.Link = Link
        for i in range(len(node)):
            GraphNode.append([])
            for j in range(len(node[i])):
                GraphNode[i].append(node[i][j])
                self.UID += str(node[i][j])

    def isEqual(self, node2):
        return self.UID == node2.UID

    def isSolution(self):
        n = len(self.GraphNode)
        for i in range(n):
            for j in range(n):
                if ( i + 1 < n ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i+1][j] ):
                        return False
                if ( i - 1 >= 0 ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i-1][j] ):
                        return False
                if ( j + 1 < n ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i][j+1] ):
                        return False
                if ( j - 1 >= 0 ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i][j-1] ):
                        return False
        return True

    def DeepCopy(self):
        node = []
        for i in range(len(self.GraphNode)):
            node.append([])
            for j in range(len(self.GraphNode[i])):
                node[i].append(self.GraphNode[i][j])
        return node

    def CalculateHeuristicDistance(self):
        n = len(self.GraphNode)
        distance = 0
        for i in range(n):
            for j in range(n):
                if ( i + 1 < n ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i+1][j] ):
                        distance += 1
                if ( i - 1 >= 0 ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i-1][j] ):
                        distance += 1
                if ( j + 1 < n ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i][j+1] ):
                        distance += 1
                if ( j - 1 >= 0 ):
                    if ( self.GraphNode[i][j] == self.GraphNode[i][j-1] ):
                        distance += 1
        return distance

    def __lt__(self, other):
        return self.distance_top < other.distance_top

    def __eq__(self, other):
        return self.distance_top == other.distance_top

class Graph:

    def __init__(self, size):
        self.size = size

    def isVisited(self, node, visit):
        for i in range(len(visit)):
            if node.isEqual(visit[i]):
                return True
        return False

    def FindAllNode(self, node):
        Children = []
        temp_node = node.DeepCopy()

        for x in range(len(temp_node)):
            for y in range(len(temp_node[x])):
                if ( x == 0 and y == 0 ):
                    if ( temp_node[x][y] == temp_node[x][y+1] or temp_node[x][y] == temp_node[x+1][y] ):
                        if ( temp_node[x][y] != temp_node[x][y+1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y+1]
                            temp_node[x][y+1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y+1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x+1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x+1][y]
                            temp_node[x+1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x+1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz
                
                elif ( x == 0 and y == (len(node.GraphNode[x])-1) ):
                    if ( temp_node[x][y] == temp_node[x][y-1] or temp_node[x][y] == temp_node[x+1][y] ):
                        if ( temp_node[x][y] != temp_node[x][y-1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y-1]
                            temp_node[x][y-1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y-1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x+1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x+1][y]
                            temp_node[x+1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x+1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                elif ( x == (len(node.GraphNode[y])-1) and y == 0 ):
                    if ( temp_node[x][y] == temp_node[x][y+1] or temp_node[x][y] == temp_node[x-1][y] ):
                        if ( temp_node[x][y] != temp_node[x][y+1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y+1]
                            temp_node[x][y+1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y+1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x-1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x-1][y]
                            temp_node[x-1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x-1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                elif ( x == (len(node.GraphNode[y])-1) and y == (len(node.GraphNode[x])-1) ):
                    if ( temp_node[x][y] == temp_node[x][y-1] or temp_node[x][y] == temp_node[x-1][y] ):
                        if ( temp_node[x][y] != temp_node[x][y-1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y-1]
                            temp_node[x][y-1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y-1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x-1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x-1][y]
                            temp_node[x-1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x-1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz
                
                elif ( x > 0 and x < len(node.GraphNode[y]) and y == 0 ):
                    if ( temp_node[x][y] == temp_node[x][y+1] or temp_node[x][y] == temp_node[x-1][y] or temp_node[x][y] == temp_node[x+1][y] ):
                        if ( temp_node[x][y] != temp_node[x+1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x+1][y]
                            temp_node[x+1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x+1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x-1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x-1][y]
                            temp_node[x-1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x-1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y+1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y+1]
                            temp_node[x][y+1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y+1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                elif ( x == 0 and y > 0 and y < len(node.GraphNode[x]) ):
                    if ( temp_node[x][y] == temp_node[x][y-1] or temp_node[x][y] == temp_node[x+1][y] or temp_node[x][y] == temp_node[x][y+1]):
                        if ( temp_node[x][y] != temp_node[x+1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x+1][y]
                            temp_node[x+1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x+1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y+1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y+1]
                            temp_node[x][y+1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y+1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y-1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y-1]
                            temp_node[x][y-1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y-1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                elif ( x > 0 and x < len(node.GraphNode[y]) and y == (len(node.GraphNode[x])-1) ):
                    if ( temp_node[x][y] == temp_node[x][y-1] or temp_node[x][y] == temp_node[x+1][y] or temp_node[x][y] == temp_node[x-1][y]):
                        if ( temp_node[x][y] != temp_node[x+1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x+1][y]
                            temp_node[x+1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x+1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x-1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x-1][y]
                            temp_node[x-1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x-1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y-1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y-1]
                            temp_node[x][y-1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y-1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                elif ( x == (len(node.GraphNode[y])-1) and y > 0 and y < len(node.GraphNode[x]) ):
                    if ( temp_node[x][y] == temp_node[x][y-1] or temp_node[x][y] == temp_node[x-1][y] or temp_node[x][y] == temp_node[x][y+1]):
                        if ( temp_node[x][y] != temp_node[x-1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x-1][y]
                            temp_node[x-1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x-1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y-1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y-1]
                            temp_node[x][y-1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y-1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y+1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y+1]
                            temp_node[x][y+1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y+1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                else:
                    if ( temp_node[x][y] == temp_node[x][y-1] or temp_node[x][y] == temp_node[x-1][y] or temp_node[x][y] == temp_node[x][y+1] or temp_node[x][y] == temp_node[x+1][y]):
                        if ( temp_node[x][y] != temp_node[x-1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x-1][y]
                            temp_node[x-1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x-1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y-1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y-1]
                            temp_node[x][y-1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y-1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x][y+1] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x][y+1]
                            temp_node[x][y+1] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x][y+1] = temp_node[x][y]
                            temp_node[x][y] = xyz

                        if ( temp_node[x][y] != temp_node[x+1][y] ):
                            xyz = temp_node[x][y]
                            temp_node[x][y] = temp_node[x+1][y]
                            temp_node[x+1][y] = xyz
                            n1 = Node(temp_node, node.step+1, [],None)
                            Children.append(n1)
                            temp_node[x+1][y] = temp_node[x][y]
                            temp_node[x][y] = xyz
                
        return Children

    def Bfs(self, root):
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
            if ( current_Node.isSolution() ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            
            Neighbours = self.FindAllNode(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                if Neighbours[i].UID not in visited:
                    queue.append(Neighbours[i])
                    visited[Neighbours[i].UID] = Neighbours[i]

    def Dfs(self, root):
        visited = {}
        stack = []
        stack.append(root)
        Count = 0

        while ( len(stack) > 0 ):
            Count += 1
            current_Node = stack.pop()
            if ( current_Node.isSolution() ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            if ( current_Node.UID in visited ):
                continue
            visited[current_Node.UID] = current_Node
            Neighbours = self.FindAllNode(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                stack.append(Neighbours[i])
        return False

    def DfsRec(self, root):
        visited = {}
        return self.DfsUtil(root, end, visited)

    def DfsUtil(self, current_node, visited):
        visited[current_node.UID] = current_node
        if ( current_node.isSolution() ):
            print("Found Match")
            return True

        Neighbours = self.FindAllNode(current_node)
        current_node.Link = Neighbours

        for i in range(len(Neighbours)):
            if Neighbours[i].UID not in visited:
                var = self.DfsUtil(Neighbours[i], end, visited) 
                if ( var == True ):
                    return var 

    def AStarAlgorithm(self, root):
        visited = {}
        q = Q.PriorityQueue()
        dist = root.CalculateHeuristicDistance()
        print("Distance: ", dist)
        root.distance = dist
        q.put((1, root))
        visited[root.UID] = root
        Count = 0

        while ( not q.empty() ):
            Count += 1
            current_Node = (q.get())[1]
            if ( current_Node.isSolution() ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            
            Neighbours = self.FindAllNode(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                
                if Neighbours[i].UID not in visited:
                    dist = Neighbours[i].CalculateHeuristicDistance()
                    Neighbours[i].distance_top = current_Node.distance_top + 1
                    Neighbours[i].distance = Neighbours[i].distance_top + dist
                    q.put((Neighbours[i].distance, Neighbours[i]))
                    visited[Neighbours[i].UID] = Neighbours[i]

        return False

if __name__ == "__main__":

    print("Enter width of the Board: ")
    N = int(input())
    gp = Graph(N)
    print("Enter Matrix: ")
    StartState = []
    for i in range(N):
        lil = list(map(int, input().split()))
        StartState.append(lil)
    Root = Node(StartState, 0, [], None)
    while True:
        print("-------Menu-------")
        print("1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. All")
        print("5. Exit")
        NumEnter = int(input())
        if ( NumEnter == 1 ):
            t1 = int(round(time()*1000))
            if ( gp.Bfs(Root) ):
                print("Found Match")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Total time taken by Bfs: ", t2-t1)
            print("")
        elif ( NumEnter == 2 ):
            t1 = int(round(time()*1000))
            if ( gp.Dfs(Root) ):
                print("Found Match")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Total time taken by Dfs: ", t2-t1)
            print("")
        elif ( NumEnter == 3 ):
            t1 = int(round(time()*1000))
            if ( gp.AStarAlgorithm(Root) ):
                print("Found Match")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Total time taken by A*: ", t2-t1)
            print("")
        elif( NumEnter == 4 ):
            t1 = int(round(time()*1000))
            if ( gp.Bfs(Root) ):
                print("Found Match for Bfs")
            else:
                print("No Match for Bfs")
            t2 = int(round(time()*1000))
            print("Total time taken by bfs: ", t2-t1)
            print("")
            t1 = int(round(time()*1000))
            if ( gp.Dfs(Root) ):
                print("Found Match for Dfs")
            else:
                print("No Match for Dfs")
            t2 = int(round(time()*1000))
            print("Total time taken by Dfs: ", t2-t1)
            print("")
            t1 = int(round(time()*1000))
            if ( gp.AStarAlgorithm(Root) ):
                print("Found Match for A*")
            else:
                print("No Match for A*")
            t2 = int(round(time()*1000))
            print("Total time taken by A*: ", t2-t1)
            print("")
        elif ( NumEnter == 5 ):
            break
        else:
            print("Please enter a valid input")

    # N = int(input())
    # gp = Graph(N)
    # StartState = [[1, 1, 2], [1, 1, 3], [2, 3, 4]]
    # Root = Node(StartState, 0, [], None)

    # if ( gp.Bfs(Root) ):
    #     print("Found Match")
    # else:
    #     print("No Match") 
    # if ( gp.Dfs(Root) ):
    #     print("Found Match")
    # else:
    #     print("No Match") 
    # if ( gp.AStarAlgorithm(Root) ):
    #     print("Found Match")
    # else:
    #     print("No Match") 
# 1 2 3 3 1 1 4 2 1 4
# 2 3 4 4 1 2 1 1 3 4
# 3 2 3 3 1 4 3 4 1 2
# 1 2 3 4 2 2 3 3 4 1
# 2 2 2 1 4 3 2 4 3 4
# 1 3 3 2 1 1 3 1 2 1
# 4 2 3 3 3 1 2 4 3 4
# 3 4 2 4 1 2 4 3 4 4
# 4 3 4 2 1 4 2 4 1 2
# 2 1 4 3 4 3 3 2 4 3
    