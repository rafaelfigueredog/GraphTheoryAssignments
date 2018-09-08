from grafo import Grafo

def recebedados():
    global vertices
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
    arestas = []

    vertices = recebedados()
    g = Grafo()
    for i in range(len(vertices)):
        g.adicionaVertice(vertices[i])
    print(g)

    return 0
    

main()