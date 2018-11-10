# Kaustav Vats (2016048)

from PopulateGraph import Populate
from Ant import Ant
import networkx as nx


class AntColonyOptimization:
    Pheromone = 5.0
    EvapRate = 0.5
    Alpha = 1.2
    Beta = 0.8
    Iterations = 100

    def __init__(self, n):
        self.N = n
        self.Ants = []
        self.GraphEdges = []
        self.CityPheromone = []
        self.Initialize()

    def Initialize(self):
        pop = Populate(self.N)
        self.GraphEdges = pop.Crr
        self.EdgePheromone = [0.0] * len(self.GraphEdges)
        self.antPopulate()

    def antPopulate(self):
        for i in range(self.N):
            AntObject = Ant(i, self.N)
            self.Ants.append(AntObject)

    def getPathDistance(self, start, stop):
        for i in range(len(self.GraphEdges)):
            edge = self.GraphEdges[i]
            if edge[0] == start and edge[1] == stop:
                return (edge[2], i)
            elif edge[0] == stop and edge[1] == start:
                return (edge[2], i)

    def PheromoneIntensity(self, i, j, tempPeromone):
        update = self.getPathDistance(i, j)
        distance = update[0]
        index = update[1]
        ph = AntColonyOptimization.Pheromone/distance
        tempPeromone[index] = [AntColonyOptimization.EvapRate*self.EdgePheromone[index] + ph, distance, index]


    def NextCity(self, index):
        CurrentAnt = self.Ants[index]
        MaxProbCity = -1
        MaxProbIndex = -1
        NormalizationValue = 0.0
        tempPheromone = [0.0] * len(self.GraphEdges)
        prob = [0]*len(self.GraphEdges)
        for i in range(self.N):
            if not CurrentAnt.Visited[i]:
                self.PheromoneIntensity(CurrentAnt.Location, i, tempPheromone)

        # for i in range(len(tempPheromone)):
        #     print(tempPheromone[i])

        for i in range(len(tempPheromone)):
            if not tempPheromone[i] == 0:
                print("tempPheromone[i][0]: ", i, tempPheromone[i][0])
                NormalizationValue += (tempPheromone[i][0]**AntColonyOptimization.Alpha)*((1.0/tempPheromone[i][1])**AntColonyOptimization.Beta)
        for i in range(len(self.GraphEdges)):
            if not tempPheromone[i] == 0:
                print("temp: ", tempPheromone[i])
                prob[i] = ((tempPheromone[i][0]**AntColonyOptimization.Alpha)*((1/tempPheromone[i][1])**AntColonyOptimization.Beta))/NormalizationValue
                if ( prob[i] > MaxProbCity ):
                    MaxProbCity = prob[i]
                    MaxProbIndex = i
        index = tempPheromone[MaxProbIndex][2]
        CurrentAnt.updateLocation(self.GraphEdges[index][1])
        # print("return: ", (tempPheromone[MaxProbIndex], index))
        return (tempPheromone[MaxProbIndex], index)


    def updatePheromone(self, pheromone):
        for i in range(self.N):
            print(pheromone[i])
            index = pheromone[i][1]
            self.EdgePheromone[index] = pheromone[i][0][0]

    def Reset(self):
        for i in range(self.N):
            self.Ants[i].reset(i)


    def ShowSolution(self):
        newGraph = []
        for i in range(len(self.GraphEdges)):
            newGraph.append((self.GraphEdges[i][0], self.GraphEdges[i][1], self.EdgePheromone[i]*100))
        print("newGraph: ", newGraph)
        Populate.ShowGraph(self, nx.Graph(), newGraph)

    def run(self):
        for i in range(AntColonyOptimization.Iterations):
            for k in range(self.N):
                Pheromone = [0]*self.N
                for j in range(self.N):
                    Pheromone[j] = self.NextCity(j)
                self.updatePheromone(Pheromone)
            self.Reset()

        self.ShowSolution()

if __name__ == "__main__":
    aco = AntColonyOptimization(4)
    aco.run()
