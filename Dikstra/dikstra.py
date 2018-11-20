from grafo_adj import Grafo


def Dijkstra(g: Grafo, u, v):

    vertices = g.N
    vertLength = len(vertices)

    # 1. 𝞫(r) ⇽ ∞, 𝞿(r) ⇽ 0, 𝞹(r) ⇽ 0 e w ⇽ u

    w = g.N.index(u)

    beta = vertLength * [float("inf")]  # distancias
    phi = vertLength * [0]  # temporario ou permanente
    pi = vertLength * [0]  # predecessor

    # 2. 𝞫(u) ⇽ 0 e 𝞿(u) ⇽ 1

    beta[w] = 0
    phi[w] = 1

    infinity = float('inf')
    
    arcosAnterior = []

    while (vertices[w] != v):

        arcosWR = [] # armazena possiveis 'r'

        for r in range(vertLength):
            if g.M[w][r] != 0:
                arcosWR.append(r)
                alfaWR = g.M[w][r]
                # 3. 𝞿(r) = 0  𝞫(r) > 𝞫(w) + 𝞪(w,r)
                if (phi[r] == 0) and (beta[r] > (beta[w] + alfaWR)):  # comparação importante.
                    beta[r] = beta[w] + alfaWR  # 𝞫(r) ⇽ 𝞫(w)+𝞪(w,r)
                    pi[r] = vertices[w]  # 𝞹(r) ⇽ w

        # Ache um vértice r* tal que:
        # 𝞿(r*) = 0, 𝞫(r*)<∞ e 𝞫(r*)=min 𝞿(r) = 0 (𝞫(r))

        minR = infinity # R é r*
        
        for r in arcosWR:
            if phi[r] == 0 and beta[r] < infinity:
                if beta[r] < minR:
                    R = r

        if R != infinity:
            phi[R] = 1
            w = R

    return                           
        

def main():
    g_p = Grafo([], [])
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z', 'M-Z', 'P-M']:
        g_p.adiciona_aresta(i)

    print(g_p)

    print(Dijkstra(g_p, 'J', 'Z'))


main()
