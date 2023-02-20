from grafo_adj import Grafo


def Dijkstra(g: Grafo, u, v):

    vertices = g.N
    vertLength = len(vertices)

    # 1. 𝞫(r) ⇽ ∞, 𝞿(r) ⇽ 0, 𝞹(r) ⇽ 0 e w ⇽ u
    w = g.N.index(u)

    beta = vertLength * [float("inf")]  # distancias
    phi = vertLength * [0]  # nós abertos
    pi = vertLength * [None]  # predecessor
    verticesAbertos = vertLength - 1

    # 2. 𝞫(u) ⇽ 0 e 𝞿(u) ⇽ 1

    beta[w] = 0
    phi[w] = 1
    infinity = float('inf')

    while (verticesAbertos != 0): # enquanto houver valor diferente de 1 em phi;

        for r in range(vertLength):
            if g.M[w][r] != 0:
                alfaWR = g.M[w][r]
                # 3. 𝞿(r) = 0  𝞫(r) > 𝞫(w) + 𝞪(w,r)
                if (phi[r] == 0) and (beta[r] > (beta[w] + alfaWR)):  # comparação importante.
                    beta[r] = beta[w] + alfaWR  # 𝞫(r) ⇽ 𝞫(w)+𝞪(w,r)
                    #pi[r] = vertices[w]  
                    pi[r] = w # 𝞹(r) ⇽ w

        # Ache um vértice r* tal que:
        # 𝞿(r*) = 0, 𝞫(r*)<∞ e 𝞫(r*)=min 𝞿(r) = 0 (𝞫(r))

        minR = infinity # R é r*
        R = 'default'
        for r in range(vertLength):
            if phi[r] == 0 and beta[r] < infinity:
                if beta[r] < minR:
                    minR = beta[r]
                    R = r
        
        if  (R != 'default'):
            phi[R] = 1
            verticesAbertos -= 1
            w = R
        else:
            break

    #ToString

    vf = g.N.index(v)
    vi = g.N.index(u)

    menorCaminho = ''

    i = 0
    while True:

        if vf == None:
            return "Não Há Caminho"
        
        if i == 0:
            menorCaminho = vertices[vf] + menorCaminho
        else:
            menorCaminho = vertices[vf] + " - " + menorCaminho
        
        vf = pi[vf]
        i += 1
        if vf == vi:
            menorCaminho = vertices[vf] + " - " + menorCaminho
            break
   
    return menorCaminho          
        

def main():
    g_p = Grafo([], [])
    
    for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'Y']:
        g_p.adiciona_vertice(i)
    for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'E-Y', 'M-T', 'P-M', 'T-Z', 'M-Z', 'Z-Y', 'Y-P']:
        g_p.adiciona_aresta(i)
    
    print()
    print(g_p)
    print( Dijkstra(g_p, 'Z', 'T'))
    print()

main()
