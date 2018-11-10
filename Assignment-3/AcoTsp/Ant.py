# Kaustav Vats (2016048)


class Ant:

    def __init__(self, loc, n):
        self.Location = -1
        self.prevLocation = -1
        self.N = n
        self.Visited = [False]*n
        self.setLocation(loc)
        self.TourCost = 0

    def setLocation(self, loc):
        self.Location = loc
        self.Visited[loc] = True

    def updateLocation(self, loc):
        self.prevLocation = self.Location
        self.setLocation(loc)

    def reset(self, loc):
        self.Location = -1
        self.prevLocation = -1
        self.Visited = [False] * self.N
        self.setLocation(loc)
        self.TourCost = 0
