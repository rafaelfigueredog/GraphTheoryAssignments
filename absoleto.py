from grafo import Grafo

def recebeVetices():
    # Questão 1 (A, D):
    vertices = input()
    vertices = vertices.split(", ")
    chave = True
    for i in vertices:
        if len(i) != 0:
            for j in i:
                if (j >= chr(65) and j <= chr(90)) or (j >= chr(97) and j <= chr(122)):
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

def recebeArestas():
    global vertices
    arestas = input()
    stringlen = len(arestas)
    
    verificador1 = 0
    verificador2 = 0
    verificador3 = 0
    # regras basicas:

    for i in arestas:
        if   ( i == "(" ):
            verificador1 += 1

        elif ( i == "-" ):
            verificador2 += 1

        elif ( i == ")" ):
            verificador3 += 1
    
    if ((verificador1 == verificador2 == verificador3) and ( (verificador1 + verificador2 + verificador3) < stringlen )):
        
        listaNomesArestas = []
        nomeAresta = ''
        vinexistente = []

        i = 0
        while (i < stringlen):

            if (arestas[i] >= chr(65) and arestas[i] <= chr(90)) or (arestas[i] >= chr(97) and arestas[i] <= chr(122)):
                arestname += arestas[i]

            else if arestas[i] == "(":
                listaNomesArestas.append(nomeAresta)
                nomeAresta = ''
                ligacao = ''
                i+=1
                while ( arestas[i] != ")" )
                    ligacao += arestas[i]
                    i += 1
                talvezvertices = ligacao.split("-")
                for i in talvezvertices:
                    if (i not in vertices):
                        vinexistente.append(i)
                # definir o que fazer quando os vertices existem (estão contidos no conjunto de vertices). Criar aresta.
                
    else:
        print("Entrada Invalida, Digite novamente seguindo o modelo: a1(A-B), a2(B-C) ... Sendo A, B e C vertices pré-existentes.")
        recebeArestas()
        
                

def naoAdjacentes(vertices, arestas):

    return 0

def main ():
    global vertices, arestas
    nArestas = 0;
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
    return 0

vertices = []
arestas = {}
main()