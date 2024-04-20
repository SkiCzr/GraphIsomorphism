from graph_io import load_graph, save_graph
from graph import *

with open(
        'C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph.gr') as f:
    G = load_graph(f)


def complement(G) -> "Graph":
    G2 = Graph(False, len(G.vertices))
    for i in range(0, len(G.vertices)):
        for j in range(0, len(G.vertices)):
            if i != j and not G.find_edge(G.vertices[i], G.vertices[j]) and not G2.find_edge(G2.vertices[i],
                                                                                             G2.vertices[j]):
                edge = Edge(G2.vertices[i], G2.vertices[j])
                G2 += edge
    return G2


with open('C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph2.gr',
          'w') as f:
    save_graph(complement(G), f)
