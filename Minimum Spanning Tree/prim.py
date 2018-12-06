from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue

def Prim(g: Grafo):

    verticeInicial = 0
    mst = Grafo() # mst = Minimum Spanning Tree
    mst.adiciona_vertice(g.N[verticeInicial])
    idx = verticeInicial

    while (mst.quantidadeVertices != g.quantidadeVertices):

        for i in range( idx, len(g.M[idx]) ):
            if (g.M[idx][i] > 0): # encontrei um vertice fora da arvore
                mst.adiciona_vertice(g.N[i]) # adiciono o vertice na arvore
                qtdeVerticesNaArvore += 1 # incremento a quantidade
                aresta = g.N[verticeInicial] + '-' + g.N[i] # crio a aresta
                tamanhoAresta = g.Mfila[idx][i].remove() # menor peso pela fila de prioridade
                mst.adiciona_aresta(aresta, tamanhoAresta)

            # fazer o algoritimo girar


        """ idxfixo = idx
        while ( (idx - 1) >= 0 ):
            if ( g.M[idx-1][idx] != str ):
                grau += g.M[idx-1][idxfixo]
            idx -= 1 """

                  


def main():

    g_p = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'Y']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'E-Y', 'M-T', 'P-M', 'T-Z', 'M-Z', 'Z-Y', 'Y-P']:
        g_p.adiciona_aresta(i)
    
    print(g_p)
    Prim(g_p)
    
    
    
    


main()