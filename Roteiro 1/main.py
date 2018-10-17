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
            invligacao = ligacao[::-1]
            for j in conjArestas:
                if ((j == invligacao) or (conjArestas.count(ligacao) > 1)):
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
        arestasNoVertice.sort()
    return arestasNoVertice

def eh_completo(g: Grafo):
    #condição1
    N = len(g.N)
    A = (N*(N-1))/2
    if (len(g.A) < A):
        return False
    else:
        return True

def conexo(g: Grafo):
    if ( (len(g.A) == 0) or (len(g.A) < (len(g.N) - 1)) ):
        return False
    else:
        nVertices = len(g.N)
        ligacoes = {}
        lenligacoes = {}
        
        for v in g.N:
            ligacoes[v] = []
            lenligacoes[v] = 0

        nConexoes = 0;
        verticeMaior = ''
        for i in g.A.keys():

            vertices = g.A[i].split("-")

            if (vertices[0] != vertices[1]):

                if vertices[1] not in ligacoes[vertices[0]]:

                    ligacoes[vertices[0]] += [vertices[1]]
                    lenligacoes[vertices[0]] += 1
                    valortemporario1 = lenligacoes[vertices[0]]

                    if valortemporario1 > nConexoes:
                        nConexoes = valortemporario1
                        verticeMaior = vertices[0]

                if vertices[0] not in ligacoes[vertices[1]]:

                    ligacoes[vertices[1]] += [vertices[0]]
                    lenligacoes[vertices[1]] += 1
                    valortemporario2 = lenligacoes[vertices[1]]

                    if valortemporario2 > nConexoes:
                        nConexoes = valortemporario2
                        verticeMaior = vertices[1]
                        
        if ( nConexoes == (nVertices - 1)):
            return True
        elif ((verticeMaior == False) or list(lenligacoes.values()).count(0) > 0):
            return False
        else:
            complementar = []
            nFaltas = 0
            for v in g.N:
                if ( (nFaltas + nConexoes) == (nVertices - 1) ):
                    break
                if (v == verticeMaior):
                    continue
                if v not in ligacoes[verticeMaior]:
                    complementar.append(v)
                    nFaltas += 1
            
            for v in ligacoes[verticeMaior]:
                if (nFaltas == 0):
                    return True
                nFaltas -= ligacoes[v].count(complementar[nFaltas-1]) # nesse ponto, não haverá repeticões.
        
        if (nFaltas == 0):
            return True
        else:
            return False