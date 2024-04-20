from graph_io import load_graph, save_graph
from graph import *

with open(
        'C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph.gr') as f:
    G1 = load_graph(f)

with open(
        'C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph.gr') as f:
    G2 = load_graph(f)


def degreesort():
    vert = []
    for v in G1.vertices:
        vert.append(v)
    for v in G2.vertices:
        vert.append(v)
    vert = sorted(vert, key=lambda x: x.degree)
    return vert


print(degreesort())
