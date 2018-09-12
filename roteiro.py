from grafo import Grafo
from itertools import product

def vertices_nao_adjacentes(g: Grafo):
    possibilidades = []
    genArestas = product(g.N, repeat=2)
    for subset in genArestas:
        aresta =  subset[0] + "-" + subset[1]
        possibilidades.append(aresta)
    naoAdjacentes = []
    for i in possibilidades:
        if (i not in g.A.values()):
            naoAdjacentes.append(i)
    return naoAdjacentes

def ha_laco(g: Grafo):
    totalarestas = len(g.A.values())
    if ( totalarestas != 0 ):
        for i in range(totalarestas):
            ligacao = list(g.A.values())[i].split("-")
            if (ligacao[0] == ligacao[1]):
                return True
        return False
    else:
        return False

def arestasParalelas(g: Grafo):
    totalarestas = len(g.A.values())
    conjArestas = list(g.A.values())
    if ( totalarestas != 0 ):
        for i in range(totalarestas):
            ligacao = conjArestas[i]
            procligacao = ligacao[::-1]
            for j in conjArestas:
                if (j == procligacao):
                    return True
        return False
    else:
        return False

def grau(g: Grafo, vetice):
    totalarestas = len(g.A.values())
    contador = 0
    if ( totalarestas != 0 and (vetice in g.N)):
        conjArestas = list(g.A.values())
        for i in range(totalarestas):
            ligacao = conjArestas[i].split("-")
            if (vetice in ligacao):
                contador += 1

    return contador

def arestas_sobre_vertice(g: Grafo, vetice):

    totalarestas = len(g.A.values())
    arestasNoVertice = []
    if (totalarestas != 0):
        for i in list(g.A.keys()):
            if (vetice in g.A[i].split("-")):
                arestasNoVertice.append(i)
    
    return arestasNoVertice

def main(): 
    g = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
main()