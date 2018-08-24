#!/usr/bin/python
# Kaustav Vats (2016048)

import queue as Q
from time import time
from math import sqrt

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
        for i in range(len(self.GraphNode)):
            for j in range(len(self.GraphNode[i])):
                if ( self.GraphNode[i][j] != node2.GraphNode[i][j] ):
                    return False
        return True
    
    def DeepCopy(self):
        node = []
        for i in range(len(self.GraphNode)):
            node.append([])
            for j in range(len(self.GraphNode[i])):
                node[i].append(self.GraphNode[i][j])
        return node

    def __str__(self):
        ans = ""
        for i in range(len(self.GraphNode)):
            ans += self.GraphNode[i] + "\n"
        return ans

    def __cmp__(self, other):
        return cmp(self.distance, other.distance)

    def __lt__(self, other):
        return self.distance_top < other.distance_top

    def __eq__(self, other):
        return self.distance_top == other.distance_top

# class NodeAStar:
    
#     def __init__(self, node, step, GraphNode, Link):
#         self.step = step
#         self.node = node
#         self.distance_top = 0
#         self.distance = 0
#         self.GraphNode = GraphNode
#         self.Link = Link
#         for i in range(len(node)):
#             GraphNode.append([])
#             for j in range(len(node[i])):
#                 GraphNode[i].append(node[i][j])

#     def isEqual(self, node2):
#         for i in range(len(self.GraphNode)):
#             for j in range(len(self.GraphNode[i])):
#                 if ( self.GraphNode[i][j] != node2.GraphNode[i][j] ):
#                     return False
#         return True
    
#     def DeepCopy(self):
#         node = []
#         for i in range(len(self.GraphNode)):
#             node.append([])
#             for j in range(len(self.GraphNode[i])):
#                 node[i].append(self.GraphNode[i][j])
#         return node

#     def toString():
#         for i in range(len(self.GraphNode)):
#             print(self.GraphNode[i])
#         print("Done")

#     def __cmp__(self, other):
#         return cmp(self.distance, other.distance)

class Graph:
    
    def __init__(self, size):
        self.size = size
        
    def isVisited(node, visit):
        for i in range(len(visit)):
            if node.isEqual(visit[i]):
                return True
        return False

    def FindZero(NodeArg):
        for i in range(len(NodeArg.GraphNode)):
            for j in range(len(NodeArg.GraphNode[i])):
                if ( NodeArg.GraphNode[i][j] == 0 ):
                    return [i, j]
        print(-1, -1)
        return [-1, -1]    

    def FindAllNode(node):
        Children = []
        temp = Graph.FindZero(node)
        x = temp[0]
        y = temp[1]
        temp_node = node.DeepCopy()

        # print("temp_node: ", temp_node)

        if ( x == 0 and y == 0 ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == 0 and y == (len(node.GraphNode[x])-1) ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == (len(node.GraphNode[y])-1) and y == 0 ):
            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == (len(node.GraphNode[y])-1) and y == (len(node.GraphNode[x])-1) ):
            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0
            
        elif ( x > 0 and x < len(node.GraphNode[y]) and y == 0 ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == 0 and y > 0 and y < len(node.GraphNode[x]) ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x > 0 and x < len(node.GraphNode[y]) and y == (len(node.GraphNode[x])-1) ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0
            
            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0
            
        elif ( x == (len(node.GraphNode[y])-1) and y > 0 and y < len(node.GraphNode[x]) ):
            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0 
            
            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

        else:
            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0 
            
            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            Children.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0
        return Children

        
    def bfs(self, root, end):
        visited = []
        queue = []
        queue.append(root)
        visited.append(root)
        Count = 0
        while ( True ):
            Count += 1
            if ( len(queue) == 0 ):
                return False
            current_Node = queue.pop(0)
            if ( current_Node.isEqual(end) ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            # if ( Graph.isVisited(current_Node, visited) ):
            #     continue
            # print("Len Queue: ", len(queue))
            # print("Count: ", Count)
            # print(current_Node.toString())
            # print("Current: ", current_Node.GraphNode)
            # print("Yes")
            Neighbours = Graph.FindAllNode(current_Node)
            current_Node.Link = Neighbours
            # for i in range(len(Neighbours)):
            #     for j in range(len(Neighbours[i].GraphNode)):
            #         print(Neighbours[i].GraphNode[j])
            #     print("")
            # current_Node.toString()
            # print("Children: ", Neighbours)

            for i in range(len(Neighbours)):
                # print("padose")
                # for j in range(len(Neighbours[i].GraphNode)):
                    # print(Neighbours[i].GraphNode[j])
                # print("done")
                if ( not Graph.isVisited(Neighbours[i], visited) ):
                    Neighbours[i].step = current_Node.step + 1
                    queue.append(Neighbours[i])
                    visited.append(Neighbours[i])
                    # print("Not Visited!")
                # else:
                    # print("Already Visited!")
    

    def Dfs(self, root, end):
        visited = []
        stack = []
        stack.append(root)
        Count = 0
        # visited.append(root)

        while ( len(stack) > 0 ):
            Count += 1
            current_Node = stack.pop()
            if ( current_Node.isEqual(end) ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            if ( Graph.isVisited(current_Node, visited) ):
                # print("lol")
                continue
            visited.append(current_Node)
            Neighbours = Graph.FindAllNode(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                # if ( not Graph.isVisited(Neighbours[i], visited) ):
                Neighbours[i].step = current_Node.step + 1
                stack.append(Neighbours[i])
                    # visited.append(Neighbours[i])
                    # print("Not Visited!")
                # else:
                    # print("Already Visited!")
        return False
            

        # return self.DfsUtil(root, end, visited)
        # if ( var == True ):
        #     return True
        # else:
        #     return False

    # def DfsUtil(self, current_node, end, visited):
    #     visited.append(current_node)
    #     if ( current_node.isEqual(end) ):
    #         print("Found Match")
    #         return True

    #     Neighbours = Graph.FindAllNode(current_node)
    #     current_node.Link = Neighbours
    #     # print("Length: ",len(Neighbours))
    #     # for i in range(len(Neighbours)):
    #     #     print("padose")
    #     #     for j in range(len(Neighbours[i].GraphNode)):
    #     #         print(Neighbours[i].GraphNode[j])
    #     #     print("done")

    #     for i in range(len(Neighbours)):
    #         if ( not Graph.isVisited(Neighbours[i], visited) ):
    #             Neighbours[i].step += current_node.step
    #             var = self.DfsUtil(Neighbours[i], end, visited) 
    #             if ( var == True ):
    #                 return var
    
    def CalculateManhattanDistance(self, node, end):
        arr = [0]*(self.size+1)
        brr = [0]*(self.size+1)
        for i in range(len(node.GraphNode)):
            for j in range(len(node.GraphNode[i])):
                arr[node.GraphNode[i][j]] = [i, j]

        for i in range(len(end.GraphNode)):
            for j in range(len(end.GraphNode[i])):
                brr[end.GraphNode[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0]-brr[i][0]) + abs(arr[i][1]-brr[i][1])
        return dist
    
    def AStarAlgorithm(self, root, end):
        visited = []
        q = Q.PriorityQueue()
        dist = self.CalculateManhattanDistance(root, end)
        root.distance = dist
        q.put((1, root))
        visited.append(root)
        Count = 0

        while ( not q.empty() ):
            Count += 1
            current_Node = (q.get())[1]
            # print("current_Node: ", current_Node)
            # print("q.get()[1]: ")
            # for j in range(len(current_Node.GraphNode)):
            #         print(current_Node.GraphNode[j])
            # print("dist_top, dist", current_Node.distance_top, current_Node.distance)
            # print("")
            if ( current_Node.isEqual(end) ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            
            Neighbours = Graph.FindAllNode(current_Node)
            current_Node.Link = Neighbours
            # for i in range(len(Neighbours)):
            #     dist = self.CalculateManhattanDistance(Neighbours[i], end)
            #     Neighbours[i].distance_top = current_Node.distance_top + 1
            #     Neighbours[i].distance = Neighbours[i].distance_top + dist

            for i in range(len(Neighbours)):
                # print("padose")
                # for j in range(len(Neighbours[i].GraphNode)):
                #     print(Neighbours[i].GraphNode[j])
                # print("done")
                if ( not Graph.isVisited(Neighbours[i], visited) ):
                    dist = self.CalculateManhattanDistance(Neighbours[i], end)
                    Neighbours[i].distance_top = current_Node.distance_top + 1
                    Neighbours[i].distance = Neighbours[i].distance_top + dist
                    Neighbours[i].step = current_Node.step + 1
                    # print(dist, Neighbours[i].distance_top)
                    # print("GraphNode: ")
                    # for j in range(len(Neighbours[i].GraphNode)):
                    #     print(Neighbours[i].GraphNode[j])
                    # print("dist_top, dist, distance", Neighbours[i].distance_top, dist, Neighbours[i].distance)
                    q.put((Neighbours[i].distance, Neighbours[i]))
                    visited.append(Neighbours[i])
                    # print("Not Visited!")
                    # Neighbours[i].toString()
                # else:
                    # print("Already Visited!")
            # print("")

        return False
    
    def IDAStar(self, root, end):
        queue = Q.PriorityQueue()
        dist = self.CalculateManhattanDistance(root, end)
        root.distance = dist
        queue.put((1, root))
        var = dist
        while True:
            var = self.IDAStarUtil(queue, end, var)
            if ( isinstance(var, bool) ):
                return True
            elif( isinstance(var, int) ):
                if ( var == -1 ):
                    return False
        
    def IDAStarUtil(self, q, end, MaxDistance):
        
        Count = 0
        CurrentDistance = -1
        # print("MaxDistance: ", MaxDistance)
        while ( not q.empty() ):
            Count += 1
            current_Node = (q.get())[1]
            # print("current_Node: ", current_Node)
            # print("q.get()[1]: ")
            # for j in range(len(current_Node.GraphNode)):
                    # print(current_Node.GraphNode[j])
            # print("dist_top, dist", current_Node.distance_top, current_Node.distance)
            # print("")
            if ( current_Node.isEqual(end) ):
                print("No of Nodes visited: ", Count)
                print("Depth: ",current_Node.step)
                return True
            # for i in range(len(current_Node.GraphNode)):
            #     print(current_Node.GraphNode[i])
            # print(current_Node.distance)
            # print("MaxDistance: ", MaxDistance)
            if ( current_Node.distance > MaxDistance ):
                # print("Continue..")
                if ( CurrentDistance != -1 and current_Node.distance < CurrentDistance ):
                    CurrentDistance = current_Node.distance
                else:
                    CurrentDistance = current_Node.distance
                continue
            # print("Why Continue...")
            Neighbours = Graph.FindAllNode(current_Node)
            current_Node.Link = Neighbours
            # for i in range(len(Neighbours)):
            #     dist = self.CalculateManhattanDistance(Neighbours[i], end)
            #     Neighbours[i].distance_top = current_Node.distance_top + 1
            #     Neighbours[i].distance = Neighbours[i].distance_top + dist

            for i in range(len(Neighbours)):
                # print("padose")
                # for j in range(len(Neighbours[i].GraphNode)):
                #     print(Neighbours[i].GraphNode[j])
                # print("done")
                dist = self.CalculateManhattanDistance(Neighbours[i], end)
                Neighbours[i].distance_top = current_Node.distance_top + 1
                Neighbours[i].distance = Neighbours[i].distance_top + dist
                Neighbours[i].step = current_Node.step + 1
                q.put((Neighbours[i].distance, Neighbours[i]))

        return CurrentDistance
    
if __name__ == "__main__":
    
    print("Enter Your Puzzle N: ")
    N = int(input())
    gp = Graph(N)
    print("Enter Start State: ")
    StartState = []
    for i in range(int(sqrt(N+1))):
        lil = list(map(int, input().split()))
        StartState.append(lil)
    print("Enter Goal State: ")
    GoalState = []
    for i in range(int(sqrt(N+1))):
        lil = list(map(int, input().split()))
        GoalState.append(lil)
    Root = Node(StartState, 0, [], None)
    End = Node(GoalState, 0, [], None)
    while True:
        print("-------Menu-------")
        print("1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. IDA*")
        print("5. All")
        print("6. Exit")
        NumEnter = int(input())
        if ( NumEnter == 1 ):
            t1 = int(round(time()*1000))
            if ( gp.bfs(Root, End) ):
                print("Found Match")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Total time taken by Bfs: ", t2-t1)
        elif ( NumEnter == 2 ):
            t1 = int(round(time()*1000))
            if ( gp.Dfs(Root, End) ):
                print("Found Match")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Total time taken by Dfs: ", t2-t1)
        elif ( NumEnter == 3 ):
            t1 = int(round(time()*1000))
            if ( gp.AStarAlgorithm(Root, End) ):
                print("Found Match")
            else:
                print("No Match")
            t1 = int(round(time()*1000))
            print("Total time taken by A*: ", t2-t1)
        elif ( NumEnter == 4 ):
            t1 = int(round(time()*1000))
            if ( gp.IDAStar(Root, End) ):
                print("Found Match")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Total time taken by IDA*: ", t2-t1)
        elif( NumEnter == 5 ):
            t1 = int(round(time()*1000))
            if ( gp.bfs(Root, End) ):
                print("Found Match for Bfs")
            else:
                print("No Match for Bfs")
            t2 = int(round(time()*1000))
            print("Total time taken by bfs: ", t2-t1)
            t1 = int(round(time()*1000))
            if ( gp.Dfs(Root, End) ):
                print("Found Match for Dfs")
            else:
                print("No Match for Dfs")
            t2 = int(round(time()*1000))
            print("Total time taken by Dfs: ", t2-t1)
            t1 = int(round(time()*1000))
            if ( gp.AStarAlgorithm(Root, End) ):
                print("Found Match for A*")
            else:
                print("No Match for A*")
            t2 = int(round(time()*1000))
            print("Total time taken by A*: ", t2-t1)
            t1 = int(round(time()*1000))
            if ( gp.IDAStar(Root, End) ):
                print("Found Match for IDA*")
            else:
                print("No Match for IDA*")
            t2 = int(round(time()*1000))
            print("Total time taken by IDA*: ", t2-t1)
        elif ( NumEnter == 5 ):
            break
        else:
            print("Please enter a valid input")
            

    # N = int(input())
    # # # N = 2
    # StartState = [[0, 2, 3], [1, 4, 5], [8, 7, 6]]
    # GoalState = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    # # # StartState = [[1, 2, 5], [3, 4, 6], [8, 7, 0]]
    # # # GoalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    # Root = Node(StartState, 0, [], None)
    # End = Node(GoalState, 0, [], None)

    # # # RootA = NodeAStar(StartState, 0, [], None)
    # # # EndA = NodeAStar(GoalState, 0, [], None)
    # gp = Graph(N)
    # # # gp.bfs(Root, End)
    # # # if ( gp.bfs(Root, End) ):
    # # #     print("Found Match")
    # # # else:
    # # #     print("No Match")
    # # print(gp.Dfs(Root, End))
    # # # gp.AStarAlgorithm(Root, End)
    # gp.IDAStar(Root, End)
    # # # gp.AStarAlgorithm(RootA, EndA)
