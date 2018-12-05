from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue

def Prim(g: Grafo):

    verticeArbitrario = 0
    VerticeNaArvore = 0

    """ while (VerticeNaArvore != g.quantidadeVertices)

        for i in g.M[verticeArbitrario]: """





def main():

    g_p = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'Y']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'E-Y', 'M-T', 'P-M', 'T-Z', 'M-Z', 'Z-Y', 'Y-P']:
        g_p.adiciona_aresta(i)
    
    print()
    print(g_p)
    print(g_p.quantidadeVertices)

   
main()