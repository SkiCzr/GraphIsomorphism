from graph_io import load_graph, save_graph, write_dot
from graph import *

with open('C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph.gr') as f:
    G1 = load_graph(f)


def BFS(G):

    # Mark all the vertices as not visited
    visited = []
    queue = []

    s = G.vertices[0]
    G.vertices[0].label = 1
    queue.append(s)
    visited.append(s)
    while queue:

        s = queue.pop(0)

        for i in s.neighbours:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                i.label = len(visited)

    if len(visited) == len(G.vertices):
        return True
    return False

print(BFS(G1))
with open('graph2.dot', 'w') as f:
    write_dot(G1, f)


with open('C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual assignment\\examplegraphs\\examplegraph.gr') as f:
    G1 = load_graph(f)

def DFS(G):

    # Mark all the vertices as not visited
    visited = []
    stack = []

    s = G.vertices[0]
    G.vertices[0].label = 1
    stack.append(s)
    visited.append(s)
    while stack:

        s = stack.pop()

        for i in s.neighbours:
            if i not in visited:
                stack.append(i)

        if s not in visited:
            visited.append(s)
            s.label = len(visited)


    if len(visited) == len(G.vertices):
        return True
    return False

print(DFS(G1))
with open('graph3.dot', 'w') as f:
    write_dot(G1, f)