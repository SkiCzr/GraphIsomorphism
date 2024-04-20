from graph import *

# G = Graph(False, 4)
# print(G)
# u = Vertex(G)
# print(u)
# v = Vertex(G)
# G.is_adjacent(u, v)
# f = Edge(v, u)
# G.add_edge(f)
# G.is_adjacent(u, v)
# print(G)
# w = Vertex(G)
# G.add_vertex(w)
# e = Edge(u, w)
# G += e
# print(e.tail)
# print(e.head)
# print(e.other_end(u))
# print(w in G.vertices)
# print(e in G.edges)
# print(u.degree)
# print(v in u.neighbours)
# x = Vertex(G, 'X')
# G += x
# print(G)
# print(x)


def createV(n):
    G = Graph(False)
    for i in range(0, n - 1, 2):
        head = Vertex(G, i)
        tail = Vertex(G, i + 1)
        G += head
        G += tail
    return G
def b1(n) -> "Graph":
    G = createV(n)
    for i in range(0, n-1):
        edge = Edge(G.vertices[i], G.vertices[i+1])
        G += edge
    return G

def b2(n) -> "Graph":
    G = b1(n)
    edge = Edge(G.vertices[n-1], G.vertices[0])
    G += edge
    return G

def b3(n) -> "Graph":
    G = createV(n)
    for i in range(0, n-1):
        for j in range(0, n-1):
            if i != j and not G.find_edge(G.vertices[i], G.vertices[j]):
                edge = Edge(G.vertices[i], G.vertices[j])
                G += edge
    return G

def b4(n,m):
    G = Graph(False)
    for i in range(0, n):
        v = Vertex(G, i)
        G += v

    for i in range(n, n + m):
        v = Vertex(G, i)
        G += v
    return G

print(b4(3,4))