from grafo import Grafo

def recebedados():
    # Questão 1 b:
    vertices = input()
    vertices = vertices.split(", ")
    chave = True
    for i in vertices:
        if len(i) != 0:
            for j in i:
                if j >= chr(65) and j <= chr(90):
                    continue
                else:
                    chave = False
                    break
        else:
            chave = False
            break

    if (chave == False):
        print("Digite novamente:")
        vertices = recebedados()
    
    return vertices

def main ():

    vertices = []
    arestas = {}

    # Questão 1 a:
    vertices = recebedados()
    g = Grafo()
    for i in range(len(vertices)):
        g.adicionaVertice(vertices[i])

    # Questão 
    for i in range(len(vertices)):
        if (i != len(vertices) - 1):
            nomeDaAresta = 'a'+str(i+1) 
            posAresta = str(vertices[i])+"-"+str(vertices[i+1])
            g.adicionaAresta(nomeDaAresta, posAresta)
            arestas[nomeDaAresta] = "("+posAresta+")"
    for i in list(arestas.keys()):
        print(str(i)+str(arestas[i]), end=", ")
    print()
    return 0
    
    
main()