from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue
import graphLibrary
import copy
import random

def Prim(g: Grafo):

    if (g.quantidadeVertices == 0):
        return None
    
    mst = Grafo() 
    raiz = ModificacaoPrim(g)
    
    raiz = random.randint(0, g.quantidadeVertices)
    print(raiz, g.N[raiz])
    mst.adiciona_vertice(g.N[4])
    
    ligacoesValidas = [0] * g.quantidadeVertices
    for i in range(g.quantidadeVertices):
        ligacoesValidas[i] = graphLibrary.grau(g, g.N[i])
    
    arestasDaFilaPrincipal = {}
    FilaPrincipal = PriorityQueue()
    
    aux = 0

    while (mst.quantidadeVertices != g.quantidadeVertices):

        for k in range( aux, len(mst.N) ):
            Vertex = mst.N[k]
            idx = g.N.index(Vertex)
            if (ligacoesValidas[idx] == 0):
                continue
            for i in range( idx, len(g.M[idx]) ):
                if (g.M[idx][i] > 0): # encontrei um vertice fora da arvore
                    v = g.N[i] # Possivel novo vertice
                    if not (mst.existe_vertice(v)):
                        pesoArestaEncontrada = g.Mfila[idx][i].seeFist()
                        arestaEncontrada = g.N[idx] + '-' + g.N[i]
                        if pesoArestaEncontrada in arestasDaFilaPrincipal.keys():
                            arestasDaFilaPrincipal[pesoArestaEncontrada].append(arestaEncontrada)
                        else:
                            arestasDaFilaPrincipal[pesoArestaEncontrada] = [arestaEncontrada]
                        FilaPrincipal.insert(pesoArestaEncontrada)

            idxfixo = idx
            while ( (idx- 1) >= 0 ):
                if (g.M[idx-1][idxfixo] > 0):
                    v = g.N[idx-1] # Possivel novo vertice
                    if not (mst.existe_vertice(v)):
                        pesoArestaEncontrada = g.Mfila[idx-1][idxfixo].seeFist()
                        arestaEncontrada = g.N[idx-1] + '-' + g.N[idxfixo]
                        if pesoArestaEncontrada in arestasDaFilaPrincipal.keys():
                            arestasDaFilaPrincipal[pesoArestaEncontrada].append(arestaEncontrada)
                        else:
                            arestasDaFilaPrincipal[pesoArestaEncontrada] = [arestaEncontrada]
                        FilaPrincipal.insert(pesoArestaEncontrada)
                idx -= 1 

        menorPesoAresta = FilaPrincipal.remove()
        novaAresta = arestasDaFilaPrincipal[menorPesoAresta].pop()

        v1 = novaAresta[0]
        v2 = novaAresta[-1]

        novoVertice = None
        if not mst.existe_vertice(v1):
            novoVertice = v1
            aux += 1
        if not mst.existe_vertice(v2):
            novoVertice = v2
            aux += 1

        if (novoVertice != None):
            mst.adiciona_vertice(novoVertice)
            mst.adiciona_aresta(novaAresta, menorPesoAresta)
            idxV1 = g.N.index(v1)
            idxV2 = g.N.index(v2)
            ligacoesValidas[idxV1] -= 1
            ligacoesValidas[idxV2] -= 1

    
    return mst

def ModificacaoPrim(g: Grafo):

    # grafo nulo retorna none

    if (g.quantidadeVertices == 0):
        return None

    # Modificação Prim
    # Objetivo é encontrar um vertice com menor peso de aresta. 

    arestasDaFilaPrincipal = {}
    menorPeso = float("inf")
    menorAresta = None

    for Vertex in range(g.quantidadeVertices):
        for edge in range( Vertex, len(g.M[Vertex])):
            if (g.M[Vertex][edge] > 0):
                pesoArestaEncontrada = g.Mfila[Vertex][edge].seeFist()
                if pesoArestaEncontrada < menorPeso:
                    menorPeso = pesoArestaEncontrada
                    menorAresta = Vertex
    
    return menorAresta
        
def main():

    grafo = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        grafo.adiciona_vertice(i)
    for i in [('J-C', 3), ('C-E', 1), ('C-P', 5), ('C-M', 4), ('C-T', 2), ('M-T', 3), ('P-M', 1), ('T-Z', 6), ('M-Z', 9)]:
        grafo.adiciona_aresta(*i)

    print("\nOriginal\n")
    print(grafo)
    print()
    print("Minimal Spanning Tree\n")
    mst = Prim(grafo)
    print(mst)
    
main()