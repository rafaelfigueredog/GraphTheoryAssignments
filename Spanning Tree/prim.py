from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue

def Prim(g: Grafo):

    verticeInicial = 0
    mst = Grafo() # mst = Spanning Tree
    mst.adiciona_vertice(g.N[verticeInicial])
    idx = verticeInicial
    licacoesValidas = [0] * g.quantidadeVertices

    while (mst.quantidadeVertices != g.quantidadeVertices):

        for i in range( idx, len(g.M[idx]) ):
            if (g.M[idx][i] > 0): # encontrei um vertice fora da arvore
                licacoesValidas[idx] = 1
                if ( g.N[i] not in mst.N):
                    mst.adiciona_vertice(g.N[i]) # adiciono o vertice na arvore
                aresta = g.N[verticeInicial] + '-' + g.N[i] # crio a aresta
                mst.adiciona_aresta(aresta)

            # fazer o algoritimo girar

        """ idxfixo = idx
        while ( (idx - 1) >= 0 ):
            if ( g.M[idx-1][idx] != str ):
                grau += g.M[idx-1][idxfixo]
            idx -= 1 """

            
def main():

    g_p = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'P-M', 'T-Z', 'M-Z']:
        g_p.adiciona_aresta(i)    
    
main()