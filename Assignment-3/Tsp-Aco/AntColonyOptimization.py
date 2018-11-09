# Kaustav Vats (2016048)

from .PopulateGraph import Populate
from .Ant import Ant


class AntColonyOptimization:
    Pheromone = 1
    EvapRate = 0.5
    Alpha = 0
    Beta = 0
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
        self.CityPheromone = [0] * len(self.GraphEdges)
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
        ph = 0
        for k in range(len(self.Ants)):
            if self.Ants[k].Location == j and self.Ants[k].prevLocation == i:
                ph += AntColonyOptimization.Pheromone/distance

        tempPeromone[index] = AntColonyOptimization.EvapRate*self.CityPheromone[index] + ph
        return distance


    def NextCity(self, index, availableCity, tempPheromone):
        CurrentAnt = self.Ants[index]
        MaxProbCity = -1
        NormalizationValue = 0
        for i in range(self.N):
            if not CurrentAnt.Visited[i]:
                self.PheromoneIntensity(CurrentAnt.Location, i, tempPheromone)
        for i in range(len(tempPheromone)):
            NormalizationValue += (tempPheromone[i]**AntColonyOptimization.Alpha)*(1/)


    # def updatePheromone(self):
    #
    #
    # def ShowSolution(self):


    def run(self):
        for i in range(AntColonyOptimization.Iterations):
            CityAvailable = [True] * self.N
            Count = self.N
            tempPheromone = [0] * len(self.GraphEdges)
            for j in range(self.N):
                self.NextCity(j, CityAvailable, tempPheromone)

            self.updatePheromone()
        self.ShowSolution()



# Note:
# Stopping condition should be when all Ants take same