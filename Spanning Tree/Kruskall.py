from grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue
import copy

def kruskall(g: Grafo):

    matrizDoGrafo = copy.deepcopy(g.M)
    arestasDaFilaPrincipal = {}
    FilaDePrioridade = PriorityQueue()
    
    for Vertex in g.N:
        idx = g.N.index(Vertex)
        for i in range( idx, len(g.M[idx]) ):
            if (matrizDoGrafo[idx][i] > 0):
                pesoArestaEncontrada = g.Mfila[idx][i].seeFist()
                arestaEncontrada = g.N[idx] + '-' + g.N[i]
                if pesoArestaEncontrada in arestasDaFilaPrincipal.keys():
                    arestasDaFilaPrincipal[pesoArestaEncontrada].append(arestaEncontrada)
                else:
                    arestasDaFilaPrincipal[pesoArestaEncontrada] = [arestaEncontrada]
                FilaDePrioridade.insert(pesoArestaEncontrada)
    
    mst = Grafo()

    while (mst.quantidadeVertices != g.quantidadeVertices):

        pesoAresta = FilaDePrioridade.remove()
        aresta = arestasDaFilaPrincipal[pesoAresta].pop()

        v1 = aresta[0]
        v2 = aresta[-1]

        arvoresDiferentes = False

        if not mst.existe_vertice(v1):
            mst.adiciona_vertice(v1)
            arvoresDiferentes = True

        if not mst.existe_vertice(v2):
            mst.adiciona_vertice(v2)
            arvoresDiferentes = True
        
        if not mst.existe_aresta(aresta):
            if (arvoresDiferentes):
                mst.adiciona_aresta(aresta, pesoAresta)

    return mst

            
def main():

    grafo = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        grafo.adiciona_vertice(i)
    for i in [('J-C', 3), ('C-E', 1), ('C-P', 5), ('C-M', 4), ('C-T', 2), ('M-T', 3), ('P-M', 1), ('T-Z', 6), ('M-Z', 9)]:
        grafo.adiciona_aresta(*i)
    
    print()
    print(grafo)
    print(kruskall(grafo))
    
main()