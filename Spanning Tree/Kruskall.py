from grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue
import copy

# 1. Determine the edges that will be sorted
# 2. Determine the number of box and the range of each box
# 3. Insert edges into the appropriate box (box with range corresponding to the edge weight)
# 3. Inside the box, sort the edges using bubble sort (I don't going do this)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def formarCaixas(maximo, minimo, b):
   
    faixa = maximo - minimo
    intervalo = faixa//b 
    caixas = {}
    aux1 = minimo
    aux2 = aux1 + intervalo
    for i in range(b):
        chave = str(aux1) + '-' + str(aux2)
        caixas[chave] = []
        aux1 = aux2 + 0.1
        aux2 += intervalo
    
    return caixas

def adicionarVerticesNaCaixa(caixas, aresta, peso):

    for j in caixas.keys():
        faixas = j.split("-")
        if peso >= float(faixas[0]) and peso <= float(faixas[-1]):
            caixas[j].append( str(peso) + str(aresta) )
            
def OrdenarCaixas(caixas):

    for i in caixas.keys():
        bubbleSort(caixas[i])

def criarMSTmodificado(g: Grafo, caixas):

    chaves = list(caixas.keys())
    chaves.sort()
    mst = Grafo()

    while (mst.quantidadeVertices != g.quantidadeVertices):
        
        for i in range(len(chaves)):

            chave = chaves[i]

            while len(caixas[chave]) != 0:

                aresta = caixas[chave].pop()
                peso = int(aresta[0])
                aresta = aresta[1:]

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
                        mst.adiciona_aresta(aresta, peso)
            
    return mst

def kruskall(g: Grafo, maximo, minimo, b):

    matrizDoGrafo = copy.deepcopy(g.M)
    arestasDaFilaPrincipal = {}
    FilaDePrioridade = []

    # modificado
    caixas = formarCaixas(maximo, minimo, b)

    for Vertex in g.N:
        idx = g.N.index(Vertex)
        for i in range( idx, len(g.M[idx]) ):
            if (matrizDoGrafo[idx][i] > 0):
                pesoArestaEncontrada = g.Mfila[idx][i].seeFist()
                arestaEncontrada = g.N[idx] + '-' + g.N[i]
                
                # modificado
                adicionarVerticesNaCaixa(caixas, arestaEncontrada, pesoArestaEncontrada)
                
                if pesoArestaEncontrada in arestasDaFilaPrincipal.keys():
                    arestasDaFilaPrincipal[pesoArestaEncontrada].append(arestaEncontrada)
                else:
                    arestasDaFilaPrincipal[pesoArestaEncontrada] = [arestaEncontrada]
                FilaDePrioridade.append(pesoArestaEncontrada)
    
    mst = Grafo()

    FilaDePrioridade.sort()
    FilaDePrioridade = FilaDePrioridade[::-1]

    # modificado
    OrdenarCaixas(caixas)

    # modificado
    mst = criarMSTmodificado(g, caixas)


    
    """ while (mst.quantidadeVertices != g.quantidadeVertices):

        pesoAresta = FilaDePrioridade.pop()
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
                mst.adiciona_aresta(aresta, pesoAresta) """

    return mst

def main():

    grafo = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        grafo.adiciona_vertice(i)
    for i in [('J-C', 3), ('C-E', 1), ('C-P', 5), ('C-M', 4), ('C-T', 2), ('M-T', 3), ('P-M', 1), ('T-Z', 6), ('M-Z', 9)]:
        grafo.adiciona_aresta(*i)
    
    print()
    print(grafo)
    print(kruskall(grafo, 9, 1, 4))
    
main()