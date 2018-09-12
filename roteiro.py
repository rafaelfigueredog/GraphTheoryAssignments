from grafo import Grafo
from itertools import product



def vertices_nao_adjacentes(g: Grafo):
    possibilidades = []
    genArestas = product(g.N, repeat=2)
    for subset in genArestas:
        aresta =  subset[0] + "-" + subset[1]
        possibilidades.append(aresta)
    print(possibilidades)
    naoAdjacentes = []
    for i in possibilidades:
        if (i not in g.A.values()):
            naoAdjacentes.append(i)
    return naoAdjacentes


def main(): 
    g = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
    print(g)
    vertices_nao_adjacentes(g)

main()