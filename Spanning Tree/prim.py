from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue
import graphLibrary
from igraph import *
import copy

def Prim(g: Grafo):

    if (g.quantidadeVertices == 0):
        return None
    
    mst = Grafo() # mst = Spanning Tree
    mst.adiciona_vertice(g.N[0]) # adiciono vertice arbitrario na arvore

    
    matrizDoGrafo = copy.deepcopy(g.M)

    # calcula o grau de todos os vertices  e coloca numa lista
    # com a mesma indexação dos vertices
    licacoesValidas = [0] * g.quantidadeVertices
    for i in range(g.quantidadeVertices):
        licacoesValidas[i] = graphLibrary.grau(g, g.N[i]) 

    while (mst.quantidadeVertices != g.quantidadeVertices):
        arestasDaFilaPrincipal = {}
        FilaPrincipal = PriorityQueue()
        for Vertex in range(mst.quantidadeVertices):
            
            idx = Vertex

            if (licacoesValidas[Vertex] == 0):
                continue
            for i in range( Vertex, len(g.M[Vertex]) ):
                if (matrizDoGrafo[Vertex][i] > 0): # encontrei um vertice fora da arvore
                    v = g.N[i] # Possivel novo vertice 
                    if not (mst.existe_vertice(v)):
                        pesoArestaEncontrada = g.Mfila[Vertex][i].seeFist()
                        arestaEncontrada = g.N[Vertex] + '-' + g.N[i]
                        arestasDaFilaPrincipal[pesoArestaEncontrada] = arestaEncontrada
                        FilaPrincipal.insert(pesoArestaEncontrada)
        
            idxfixo = idx 
            while ( (idx- 1) >= 0 ):
                if (matrizDoGrafo[idx-1][idxfixo] > 0):
                    v = g.N[idx-1] # Possivel novo vertice 
                    if not (mst.existe_vertice(v)):
                        pesoArestaEncontrada = g.Mfila[idx-1][idx].seeFist()
                        arestaEncontrada = g.N[idx-1] + '-' + g.N[idxfixo]
                        arestasDaFilaPrincipal[pesoArestaEncontrada] = arestaEncontrada
                        FilaPrincipal.insert(pesoArestaEncontrada)
                idx -= 1
        
        menorPesoAresta = FilaPrincipal.remove()
        novoVertice = arestasDaFilaPrincipal[menorPesoAresta][-1]
        novaAresta = arestasDaFilaPrincipal[menorPesoAresta]
        idxV1 = g.N.index(novaAresta[0])
        idxV2 = g.N.index(novaAresta[-1])
        mst.adiciona_vertice(novoVertice)
        mst.adiciona_aresta(novaAresta, menorPesoAresta)
        licacoesValidas[idxV1] -= 1
        licacoesValidas[idxV2] -= 1
        matrizDoGrafo[idxV1][idxV2] -= 1

    return mst


        

        

            
def main():

    grafo = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        grafo.adiciona_vertice(i)
    for i in [('J-C', 3), ('C-E', 1), ('C-P', 5), ('C-M', 4), ('C-T',2), ('M-T', 3), ('P-M', 1), ('T-Z', 6), ('M-Z', 9)]:
        grafo.adiciona_aresta( *i )

    print("\nOriginal\n")
    print(grafo)
    print()
    print("Minimal Spanning Tree\n")
    print(Prim(grafo))
    
    
main()