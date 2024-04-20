import copy

from graph_io import load_graph, save_graph, write_dot
from graph import *

with open('C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual '
          'assignment\\SampleGraphsBasicColourRefinement\\colorref_largeexample_6_960.grl') as f:
    L = load_graph(f, read_list=True)


def checkNeighbours(v1, v2):
    if len(v1.neighbours) != len(v2.neighbours):
        return False
    l1 = []
    l2 = []
    for i in range(0, len(v1.neighbours)):
        l1.append(v1.neighbours[i].label)
        l2.append(v2.neighbours[i].label)

    return sorted(l1) == sorted(l2)


def colorRefinement(graphlist):
    iterList = []
    for graph in graphlist:
        iterList.append(singleRef(graph))
    izos = []
    checked = []
    print('Sets of possibly isomorphic graphs:')
    for i in range(0, len(graphlist)):
        if i not in checked:
            checked.append(i)
            izos.append(i)
            for g in graphlist:
                if graphlist.index(g) not in checked and compareGraphs(graphlist[i], g):
                    checked.append(graphlist.index(g))
                    izos.append(graphlist.index(g))
            resPrint(izos, iterList[i][0], iterList[i][1])
        izos = []
    print(iterList)





def resPrint(izos, iterations, discrete):
    type = ' '
    if discrete:
        type = 'discrete'
    print(izos, iterations, type)



def singleRef(g):
    colors = {}
    colorsMid = {}
    iterations = 0
    for vertex in g.vertices:

        colors[vertex] = 1
        vertex.label = 1

    while colors != colorsMid:
        colorsMid = copy.copy(colors)
        gr = copy.copy(g)
        iterations += 1
        for i in range(0, len(g.vertices)):
            for j in range(i + 1, len(g.vertices)):
                v11 = gr.vertices[i]
                v12 = gr.vertices[j]
                v1 = g.vertices[i]
                v2 = g.vertices[j]
                if colorsMid[v1] == colorsMid[v2] and checkNeighbours(v11, v12):
                    colors[v2] = colors[v1]
                    v2.label = v1.label
                else:
                    colors[v2] = colors[v1] + 1
                    v2.label = int(v1.label) + 1
    print(g.vertices)
    return iterations, len(set(colors.values())) == len(colors)

def compareGraphs(g, g1):
    gdict = {}
    g1dict = {}
    if len(g) != len(g1):
        return False
    for i in range(0, len(g)):
        if g.vertices[i].label in gdict:
            gdict[g.vertices[i].label] += 1
        else:
            gdict[g.vertices[i].label] = 1
        if g1.vertices[i].label in g1dict:
            g1dict[g1.vertices[i].label] += 1
        else:
            g1dict[g1.vertices[i].label] = 1
    return gdict == g1dict


colorRefinement(L[0])

for v in L[0][0].vertices:
    v.colornum = int(v.label)
with open('colorful.dot','w') as f: write_dot(L[0][0],f)

