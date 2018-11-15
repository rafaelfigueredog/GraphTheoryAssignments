from grafo_adj import Grafo
from numpy import infty
from dikstradic import dijkstra

def Dijkstra(g: Grafo, vi, vf):

    beta = [] # disancias
    pi = [] # predecessor
    phi = [] # temporario ou permanente

    w = vi

    for i in range(len(g.N)):
        if g.N[i] == vi:
            w = i
            beta.append(0)
            phi.append(1)
        else:
            beta.append(infty)
            phi.append(0)
        pi.append(0)
    
    for j in g.M[w]:
        if g.M[w][j] != 0: 
            if beta[j] > g.M[w][j]:
                beta[j] = g.M[w][j]



def main():

    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        g_p.adiciona_aresta(i) 

    print( Dijkstra(g_p, 'J', 'C')  )

main()