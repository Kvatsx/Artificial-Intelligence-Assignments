#!/usr/bin/python
# Kaustav Vats (2016048)

import networkx as nx
from random import randint as randi
import matplotlib.pyplot as plt

class Populate:
    G = nx.Graph()

    def __init__(self, n):
        self.N = n
        self.Crr = []
        self.randomPopulation()

    def randomPopulation(self):
        for i in range(self.N):
            for j in range(self.N):
                if i != j:
                    z = randi(1, self.N * 10)
                    self.Crr.append((i, j, z))

        print("Crr: ", self.Crr)
        self.G.add_weighted_edges_from(self.Crr)
        self.ShowGraph()

    def ShowGraph(self):
        # pos = nx.shell_layout(self.G)
        # pos = nx.kamada_kawai_layout(self.G)
        # pos = nx.rescale_layout(self.G)
        pos = nx.spring_layout(self.G)
        # pos = nx.spectral_layout(self.G)
        # pos = nx.random_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, node_size=100)
        nx.draw_networkx_labels(self.G, pos, font_size=13, font_family='sans-serif')
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, label_pos=0.3)

        nx.draw(self.G, pos)
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    pop = Populate(4)
