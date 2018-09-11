from grafo import Grafo
from itertools import permutations

def vertices_nao_adjacentes(g: Grafo):
    preprocessamento = permutations(g.N)
    print(g.N)