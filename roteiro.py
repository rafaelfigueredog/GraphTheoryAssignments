from grafo import Grafo
from itertools import product
from itertools import permutations

def vertices_nao_adjacentes(g: Grafo):
    naoAdjacentes = []
    genArestas = product(g.N, repeat=2)
    for subset in genArestas:
        aresta =  subset[0] + "-" + subset[1]
        if ((aresta not in list(g.A.values())) and (aresta[::-1] not in list(g.A.values()))):
            naoAdjacentes.append(aresta)
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

def ha_paralelas(g: Grafo):
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
        chave = True
        for i in range(totalarestas):
            ligacao = conjArestas[i].split("-")
            coeficiente = ligacao.count(vetice)
            if (coeficiente == 1):
                contador += 1
            elif (coeficiente == 2 and (chave) ) :
                contador += 1
                chave = False
    return contador

def arestas_sobre_vertice(g: Grafo, vetice):

    totalarestas = len(g.A.values())
    arestasNoVertice = []
    if (totalarestas != 0):
        for i in list(g.A.keys()):
            if (vetice in g.A[i].split("-")):
                arestasNoVertice.append(i)
    
    return arestasNoVertice

def eh_completo(g: Grafo):
    #condição1
    N = len(g.N)
    A = (N*(N-1))/2
    if (len(g.A) < A):
        return False
    else:
        return True

    

""" def main():

    g = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
    print(vertices_nao_adjacentes(g))
    eh_completo(g)
    g2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
    print(grau(g2, 'A'))


main() """