from grafo_adj_nao_dir import *
from roteiro2 import grau

def test_caminho_euleriano(g: Grafo):

    grauImpar = 0
    for i in g.N:
        grau = grau(g,i)
        grauImpar += grau % 2

    if (grauImpar == 2 or grauImpar == 0):
        return True
    

def main():

    

#main()