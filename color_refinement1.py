import copy
import time

from graph_io import load_graph, save_graph, write_dot
from graph import *

with open('C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual '
          'assignment\\SampleGraphsBasicColourRefinement\\colorref_largeexample_6_960.grl') as f:
    L = load_graph(f, read_list=True)


def singleRefinement(graph):
    count = 1
    newCount = 0
    graphCheck = {}
    iterations = 0
    tt = 0
    for vertex in graph:
        vertex.label = vertex.degree

    for vertex in graph:
        neighs = []
        for n in vertex.neighbours:
            neighs.append(n.label)
        graphCheck[vertex] = sorted(neighs)

    while count != newCount:
        iterations += 1
        count = newCount
        uniqueColors = set()

        for vertex in graph:
            start_time = time.time()
            vertex.label = listToStr(graphCheck[vertex])
            end_time = time.time()
            uniqueColors.add(vertex.label)

        tt += end_time - start_time
        for vertex in graph:
            neighs = []
            for n in vertex.neighbours:
                neighs.append(n.label)
            graphCheck[vertex] = sorted(neighs)
        newCount = len(uniqueColors)

    print('singeRefinement time:', tt)
    return sorted(uniqueColors), iterations, len(uniqueColors) == len(graphCheck)

def listToStr(l):
    result = ""
    for nr in l:
        result += str(nr)
    return hash(frozenset(l))

def colorRefinement(graphlist):
    izos = {}
    disc = []
    iterations = []
    start_time = time.time()
    for i in range(0, len(graphlist)):
        setto, iters, discrete = singleRefinement(graphlist[i])
        disc.append(discrete)
        iterations.append(iters)
        if hash(frozenset(setto)) in izos:
            izos[hash(frozenset(setto))].append(i)
        else:
            izos[hash(frozenset(setto))] = []
            izos[hash(frozenset(setto))].append(i)
    for v in izos.values():
        if disc[v[0]]:
            print(v, iterations[v[0]], "discrete")
        else:
            print(v, iterations[v[0]])
    end_time = time.time()
    print('Total time:', end_time - start_time)
#singleRefinement(L[0][0])
colorRefinement(L[0])




for v in L[0][0].vertices:
    v.colornum = int(v.label)
with open('colorful.dot','w') as f: write_dot(L[0][0], f)

