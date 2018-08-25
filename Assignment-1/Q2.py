#!/usr/bin/python
# Kaustav Vats (2016048)

from time import time

class Node:
    
    def __init__(self, node, step, GraphNode, Link):
        self.UID = ""
        self.step = step
        self.node = node
        self.GraphNode = GraphNode
        self.Link = Link
