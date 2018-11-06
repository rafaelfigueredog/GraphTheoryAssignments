from grafo_adj import Grafo
from numpy import infty



def Dijkstra(g: Grafo, vi, vf):

    Distancias = {}

    for i in g.N:

        if i == vi:
            Distancias[str(i)] = 0
        else:
            Distancias[str(i)] = infty
    

    





def main():

    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        g_p.adiciona_aresta(i) 


    Dijkstra(g_p, 'C', 'Z')


main()