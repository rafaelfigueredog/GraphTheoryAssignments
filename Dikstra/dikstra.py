from grafo_adj import Grafo

def Dijkstra(g: Grafo, u, v):

    vertices = g.N
    vertLength = len(vertices)
    
    # 1. 𝞫(r) ⇽ ∞, 𝞿(r) ⇽ 0, 𝞹(r) ⇽ 0 e w ⇽ u
    # 2. 𝞫(u) ⇽ 0 e 𝞿(u) ⇽ 1

    w = g.N.index(u)

    beta = vertLength*[ float("inf") ] # distancias
    phi = vertLength*[0] # temporario ou permanente
    pi = vertLength*[0] # predecessor

    beta[w] = 0
    phi[w] = 1

    # 3. 𝞿(r) = 0  𝞫(r) > 𝞫(w) + 𝞪(w,r)
    while ( vertices[w] != v ):

        candidatoAsterisco = float('inf')
        R = -1
        for r in g.M[w]:
            if g.M[w][r] != 0:
                alfaWR = g.M[w][r]
                if  (phi[r] == 0) and ( beta[r] > (beta[w] + alfaWR) ): # comparação importante.
                    
                    # 𝞫(r) ⇽ 𝞫(w)+𝞪(w,r)
                    # 𝞹(r) ⇽ w

                    beta[r] = beta[w] + alfaWR
                    pi[r] = vertices[w]

                    # Ache um vértice r* tal que:
                    # 𝞿(r*) = 0, 𝞫(r*)<∞ e 𝞫(r*)=min 𝞿(r) = 0 ( 𝞫(r) )

                    if beta[r] < candidatoAsterisco:
                        candidatoAsterisco = beta[r]
                        R = r
        if (R >= 0):
            phi[R] = 1
            w = R
    
    
    




def main():

    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        g_p.adiciona_aresta(i) 

    print(g_p)

    print( Dijkstra(g_p, 'J', 'Z')  )

main()
