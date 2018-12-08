from  grafo_adj_nao_dir import Grafo
from PriorityQueue import PriorityQueue

def kruskall(g: Grafo):


            
def main():

    g_p = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'Y']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'E-Y', 'M-T', 'P-M', 'T-Z', 'M-Z', 'Z-Y', 'Y-P']:
        g_p.adiciona_aresta(i)
    
    print(g_p)
    Prim(g_p)
    
main()