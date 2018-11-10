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
        self.ShowGraph(self.G, self.Crr)

    def ShowGraph(self, graph, crr):
        graph.add_weighted_edges_from(crr)
        # pos = nx.shell_layout(self.G)
        # pos = nx.kamada_kawai_layout(self.G)
        # pos = nx.rescale_layout(self.G)
        pos = nx.spring_layout(graph)
        # pos = nx.spectral_layout(self.G)
        # pos = nx.random_layout(self.G)
        nx.draw_networkx_nodes(graph, pos, node_size=100)
        nx.draw_networkx_labels(graph, pos, font_size=13, font_family='sans-serif')
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, label_pos=0.3)

        nx.draw(graph, pos)
        plt.axis('off')
        # plt.show()


if __name__ == "__main__":
    pop = Populate(4)
