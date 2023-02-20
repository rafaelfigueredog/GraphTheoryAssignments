from grafo_adj_nao_dir import Grafo


def grau(g:Grafo, vertice):

    if ( len(g.N) == 0 ):
        return 0
    else:
        grau = 0
        idx = g.N.index(vertice)
        for i in range( idx, len(g.M[idx]) ):
            grau += g.M[idx][i]
        idxfixo = idx
        while ( (idx - 1) >= 0 ):
            if ( g.M[idx-1][idx] != str ):
                grau += g.M[idx-1][idxfixo]
            idx -= 1

    return grau


def caminho_euleriano(g: Grafo):

    contGrauImpar = 0
    for i in g.N:
        var = grau(g,i)
        if ( ( var % 2 ) != 0 ):
            contGrauImpar += 1

    if (contGrauImpar == 2 or contGrauImpar == 0):
        return True
    
    return False
