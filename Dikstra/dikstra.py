from grafo_adj import Grafo
from numpy import infty

def Dijkstra(g: Grafo, vi, vf):

    distancias = []
    predecessor = []
    for i in range(len(g.N)):
        if g.N[i] == vi:
            distancias.append(0)
        else:
            distancias.append(infty)
        predecessor.append("undefined")
    print(distancias)
    print(predecessor)


def main():

    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        g_p.adiciona_aresta(i) 

    Dijkstra(g_p, 'C', 'Z')

main()