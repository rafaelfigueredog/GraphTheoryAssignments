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


def main(): 
    g = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
    vertices_nao_adjacentes(g)
    # teste 1
    if (ha_laco(g)):
        print("SIM")
    else:
        print("NÃO")

main()