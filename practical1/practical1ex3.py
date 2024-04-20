from graph_io import load_graph, save_graph, write_dot
from graph import *

with open(
        'C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph.gr') as f:
    G1 = load_graph(f)

with open('graph1.dot', 'w') as f:
    write_dot(G1, f)
