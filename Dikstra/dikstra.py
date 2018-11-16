from grafo_adj import Grafo
from dikstradic import dijkstra

def Dijkstra(g: Grafo, vi, vf):

    beta = [] # disancias
    pi = [] # predecessor
    phi = [] # temporario ou permanente

    vertices = g.N
    w = g.N.index[vi]

    # 1. 𝞫(u) ⇽ 0 e 𝞿(u) ⇽ 1
    # 2. 𝞫(r) ⇽ ∞, 𝞿(r) ⇽ 0, 𝞹(r) ⇽ 0 e w ⇽ u

    for i in range(len(g.N)):
        if g.N[i] == vi:
            w = i
            beta.append(0)
            phi.append(1)
        else:
            beta.append(float('inf'))
            phi.append(0)
        pi.append(0)

    # 3. 𝞿(r) = 0  𝞫(r) > 𝞫(w) + 𝞪(w,r)

    for r in g.M[w]:
        if g.M[w][r] != 0:
            alfa_w_r = g.M[w][r] 
            if ( phi[r] = 0 and  beta[r] > ( beta[w] + alfa_w_r ) ): 
                # 𝞫(r) ⇽ 𝞫(w)+𝞪(w,r) 
                # 𝞹(r) ⇽ w
                beta[r] = beta[w] + alfa_w_r
                phi[r] = vertices[w]



def main():

    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        g_p.adiciona_aresta(i) 

    print( Dijkstra(g_p, 'J', 'Z')  )

main()