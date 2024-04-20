import hashlib
import time

from graph_io import load_graph



def singleRefinement(graph):
    count = 1
    newCount = 0
    graphCheck = {}
    iterations = 0
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
        uniqueColors = []

        for vertex in graph:
            vertex.label = hash(tuple(graphCheck[vertex]))
            uniqueColors.append(vertex.label)


        for vertex in graph:
            neighs = []
            for n in vertex.neighbours:
                neighs.append(n.label)
            graphCheck[vertex] = sorted(neighs)
        newCount = len(set(uniqueColors))

    return sorted(uniqueColors), iterations, len(set(uniqueColors)) == len(graphCheck)


def basic_colorref(graphfile):
    with open(graphfile) as f:
        L = load_graph(f, read_list=True)
    graphlist = L[0]

    izos = {}
    disc = []
    iterations = []
    result = []
    for i in range(0, len(graphlist)):
        setto, iters, discrete = singleRefinement(graphlist[i])
        disc.append(discrete)
        iterations.append(iters)
        if hash(tuple(setto)) in izos:
            izos[hash(tuple(setto))].append(i)
        else:
            izos[hash(tuple(setto))] = []
            izos[hash(tuple(setto))].append(i)
    for vl in izos.values():
        result.append(tuple([sorted(vl), iterations[vl[0]], disc[vl[0]]]))
    return result


def printer(res):
    for iz in res:
        print(iz[0], iz[1], iz[2])

start_time = time.time()
printer(basic_colorref('C:\\Users\\vinte\\Desktop\\University\\Module 7\\Individual '
          'assignment\\SampleGraphsFastColorRefinement\\threepaths5120.gr'))
end_time = time.time()
print('Time:', end_time - start_time)