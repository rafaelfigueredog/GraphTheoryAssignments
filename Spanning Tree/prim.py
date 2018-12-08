from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue
import graphLibrary
from igraph import *

def Prim(g: Grafo):

    if (g.quantidadeVertices == 0):
        return None
    
    mst = Grafo() # mst = Spanning Tree
    mst.adiciona_vertice(g.N[0]) # adiciono vertice arbitrario na arvore

    # calcula o grau de todos os vertices  e coloca numa lista
    # com a mesma indexação dos vertices
    licacoesValidas = [0] * g.quantidadeVertices
    for i in range(g.quantidadeVertices):
        licacoesValidas[i] = graphLibrary.grau(g, g.N[i]) 

    while (mst.quantidadeVertices != g.quantidadeVertices):
        arestasDaFilaPrincipal = {}
        FilaPrincipal = PriorityQueue()
        for idx in range(mst.quantidadeVertices):
            if (licacoesValidas[idx] == 0):
                continue
            for i in range( idx, len(g.M[idx]) ):
                if (g.M[idx][i] > 0): # encontrei um vertice fora da arvore
                    v = g.N[i] # Possivel novo vertice 
                    if not (mst.existe_vertice(v)):
                        pesoArestaEncontrada = g.Mfila[idx][i].seeFist()
                        arestaEncontrada = g.N[idx] + '-' + g.N[i]
                        arestasDaFilaPrincipal[pesoArestaEncontrada] = arestaEncontrada
                        FilaPrincipal.insert(pesoArestaEncontrada)
        
            idxfixo = idx
            while ( (idx - 1) >= 0 ):
                if (g.M[idx-1][idxfixo] > 0):
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
        mst.adiciona_vertice(novoVertice)
        mst.adiciona_aresta(novaAresta, menorPesoAresta)
        licacoesValidas[idxfixo] -= 1
    
    return mst


        

        

            
def main():

    grafo = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        grafo.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'P-M', 'T-Z', 'M-Z']:
        grafo.adiciona_aresta(i)

    print("\nOriginal\n")
    print(grafo)
    print()
    print("Minimal Spanning Tree\n")
    print(Prim(grafo))
    
    
main()