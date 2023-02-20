def dijkstra(vertices, arestas, u, v):
    beta = {}
    phi = {}
    pi = {}

    # PASSO 2:
    for i in range(len(vertices)):
        beta[vertices[i]] = float('inf')
        phi[vertices[i]] = 0
        pi[vertices[i]] = 0

    # PASSO 1:
    beta[u] = 0
    phi[u] = 1
    pi[u] = "-"
    w = u

    verificacao = 0
    while (w != v):
        # PASSO 3:
        verificacao2 = 0
        for ligacoes in arestas:
            if (ligacoes[0] == w):
                if phi[ligacoes[2]] == 0 and beta[ligacoes[2]] > beta[w] + 1:
                    beta[ligacoes[2]] = beta[w] + 1
                    pi[ligacoes[2]] = w
                    verificacao2 += 1

        # PASSO 4:
        minimoBeta = float('inf')
        for vertice in vertices:
            if phi[vertice] == 0 and beta[vertice] < float('inf'):
                if beta[vertice] < minimoBeta:
                    minimoBeta = beta[vertice]

        if verificacao2 == 0 and minimoBeta == float('inf'):
            verificacao += 1
            break

        for vertice in vertices:
            if beta[vertice] == minimoBeta and phi[vertice] == 0 and beta[vertice] < float('inf'):
                phi[vertice] = 1
                w = vertice
                break

    if verificacao == 1:
        return False

    else:
        # PEGANDO OS ANTECESSORES
        atual = v
        lista = []
        while atual != u:
            for aaa in pi:
                if aaa == atual:
                    lista.append(atual)
                    atual = pi[atual]
                    break

        lista.append(atual)

        return len(lista) - 1, lista[::-1]


def dijkstraCarga(vertices, arestas, u, v, carga, pontosRecarga):
    inicial = u
    pontosRecarga.insert(0, u)
    pontosRecarga.append(v)

    # if dijkstra(vertices, arestas, u, v)[0] <= carga:
    #     return dijkstra(vertices, arestas, u, v)[1]
    #
    # else:
    possibilidades = {}

    for i in range(len(pontosRecarga)):
        for j in range(len(pontosRecarga)):
            if u == pontosRecarga[j] or dijkstra(vertices, arestas, u, pontosRecarga[j]) == False:
                continue
            caminho = dijkstra(vertices, arestas, u, pontosRecarga[j])[0]
            if caminho <= carga:
                possibilidades[u + "-" + pontosRecarga[j]] = caminho
        u = pontosRecarga[i]
        if i > 0:
            carga = 5

    lista = dijkstra(pontosRecarga, possibilidades, inicial, v)

    if lista == False:
        return "Não há caminho possíveis !!"

    caminhoFinal = []
    for i in range(len(lista[1])-1):
        caminhoFinal.append(dijkstra(vertices, arestas, lista[1][i], lista[1][i+1])[1])

    Final = []

    for i in range(len(caminhoFinal)):
        for j in range(len(caminhoFinal[i])):
            if (caminhoFinal[i][j] not in Final):
                Final.append(caminhoFinal[i][j])

    return Final


vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g"]
arestas = {"A-B": 1, "A-C": 1, "A-D": 1, "B-E": 1, "B-I": 1, "C-G": 1, "D-C": 1, "D-H": 1, "E-F": 1, "F-B": 1, "F-J": 1,
           "G-F": 1, "G-J": 1, "G-K": 1, "H-G": 1, "H-L": 1, "I-M": 1, "J-I": 1, "J-N": 1, "K-O": 1, "L-P": 1, "M-Q": 1,
           "M-S": 1, "N-R": 1, "N-S": 1, "N-T": 1, "O-S": 1, "P-T": 1, "Q-U": 1, "R-Q": 1, "R-V": 1, "S-R": 1, "S-X": 1,
           "U-Y": 1, "U-Z": 1, "V-b": 1, "V-Z": 1, "V-W": 1, "W-S": 1, "X-c": 1, "Y-a": 1, "a-e": 1, "c-e": 1,
           "c-W": 1, "e-f": 1, "e-g": 1, "T-S": 1}

print(dijkstraCarga(vertices, arestas, "A", "g", 5, ['L', 'S', 'U', 'a']))
print(dijkstraCarga(vertices, arestas, "A", "g", 4, ['L', 'S', 'U', 'a']))
print(dijkstraCarga(vertices, arestas, "A", "g", 3, ['L', 'S', 'U', 'a']))
print(dijkstraCarga(vertices, arestas, "A", "g", 2, ['L', 'S', 'U', 'a']))
print(dijkstraCarga(vertices, arestas, "A", "d", 1, ['L', 'S', 'U', 'a']))