import networkx as nx

def ler_arquivo_grafo(arquivo):
    with open(arquivo, 'r') as f:
        arestas = f.readlines()
    arestas = [tuple(map(int, linha.strip().split())) for linha in arestas]
    grafo = nx.Graph(arestas)
    return grafo

def dfs_caminho(grafo, inicio, fim):
    visitados = set()
    caminho = []

    def dfs(vertice):
        nonlocal visitados, caminho
        visitados.add(vertice)
        caminho.append(vertice)

        if vertice == fim:
            return True

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                if dfs(vizinho):
                    return True

        caminho.pop()
        return False

    dfs(inicio)
    return caminho if caminho[-1] == fim else None

grafo = ler_arquivo_grafo('Arestas.txt')
caminho = dfs_caminho(grafo, 0, 699)

if caminho:
    print('Caminho:', caminho)
    print('\n')
    print(len(caminho))
else:
    print('Não há caminho entre os vértices especificados.')