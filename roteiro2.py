from grafo_adj_nao_dir import *
from grafo import Grafo as G

def convertToMatrizAdj(g: G):
    N = g.N
    m = []
    coeficiente = 0
    for i in range(len(N)):
        lenVertices = len(N)
        linha = (coeficiente*['-']) + (lenVertices-coeficiente)*[0]
        coeficiente+=1
        m.append(linha)
    arestas = list(g.A.values())

    for i in range(len(arestas)):
        ligacao = arestas[i].split("-")
        indice1 = N.index(ligacao[0])
        indice2 = N.index(ligacao[1])

        if (indice1 <= indice2): 
            m[indice1][indice2] += 1
        else:
            m[indice2][indice1] += 1

    return N, m

def vertices_nao_adjacentes(g: Grafo):

    if ( len(g.N) == 0 ): 
        return False
    else:
        
        idxvertice = 0
        idxfinal = len(g.N)
        naoAdjacentes = ''

        for i in range(len(g.M)):
            for j in range(idxvertice, idxfinal):
                if (g.M[i][j] == 0):
                    naoAdjacentes += g.N[i] + "-" + g.N[j] + ", "
    return naoAdjacentes

def ha_laco(g: Grafo):

    if (len(g.N) == 0):
        return False
    else:
        for i in range(len(g.N)):
            if (g.M[i][i] > 0):
                return True

    return False


def ha_paralelas(g: Grafo):
    
    return

def grau(g: Grafo, vetice):

    return

def arestas_sobre_vertice(g: Grafo, vetice):

    return

def eh_completo(g: Grafo):

    return

def conexo(g: Grafo):

    return 
pass

def main():

    g = G(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-C', 'a3':'C-C', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
    N, m = convertToMatrizAdj(g)
    grafoMatriz = Grafo(N,m)
    print(ha_laco(grafoMatriz))
    print()
    print(grafoMatriz)
    print(vertices_nao_adjacentes(grafoMatriz))

main()