from grafo_adj import Grafo

def warshall(g: Grafo):
	
    E = g.M.copy()
    n = len(g.N)

    for i in range(1, n):
        for j in range(1, n):
            if E[j][i] == 1:
                for k in range(1, n):
                    E[j][k] = max(E[j][k],E[i][k])

    
    return E


def main():

    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        g_p.adiciona_aresta(i)
    
    print(g_p)
    E = warshall(g_p)
    for i in range(len(E)):
        for j in range(len(E)):
            print(E[i][j], end=" ")
        print()

main()