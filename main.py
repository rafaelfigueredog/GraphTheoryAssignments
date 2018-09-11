from grafo import Grafo

def recebeVetices():
    # Questão 1 (A, D):
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
        print("Por favor, siga o modelo: V1, V2, V3, ... Vn")
        print("Apenas caracteres ou array de caracteres do alfabeto em caixa alta serão aceitos: A-Z ")
        vertices = recebeVetices()
   
    return vertices

def recebeArestas(vertices):

    print(vertices, "\n")
    n = int(input("Numero de arestas:"))
    conjArestas = []
    print("Digite os vertices separados por ""-""")
    for i in range(n):
        aresta = input()
        conjArestas.append(aresta)
    
    print(conjArestas)
    pass 
def naoAdjacentes(vertices, arestas):

    return 0

def main ():

    nArestas = 0;
    vertices = []
    arestas = {}

    # Questão 1 A:
    vertices = recebeVetices()
    g = Grafo()
    for i in range(len(vertices)):
        g.adicionaVertice(vertices[i])

    # Questão 1 C
    for i in range(len(vertices)):
        if (i != len(vertices) - 1):
            nomeDaAresta = 'a'+str(i+1) 
            posAresta = str(vertices[i])+"-"+str(vertices[i+1])
            g.adicionaAresta(nomeDaAresta, posAresta)
            arestas[nomeDaAresta] = "("+posAresta+")"
    for i in list(arestas.keys()):
        print(str(i)+str(arestas[i]), end=", ")
    print()

    listArestas  = recebeArestas(vertices) 
    return 0
    

main()