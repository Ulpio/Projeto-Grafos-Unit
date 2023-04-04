import networkx as nx

# Função para ler o arquivo e converter em um grafo
def ler_arquivo_grafo(arquivo):
    with open(arquivo, 'r') as f:
        arestas = f.readlines()
    arestas = [tuple(map(int, linha.strip().split())) for linha in arestas]
    grafo = nx.Graph(arestas)
    return grafo

# Função que traça um caminho usando DFS
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

# Exemplo de uso
grafo = ler_arquivo_grafo('Arestas.txt')  # lê o arquivo e cria o grafo
caminho = dfs_caminho(grafo, 0, 689)  # traça o caminho entre os vértices 1 e 6 usando DFS

if caminho:
    print('Caminho:', caminho)
else:
    print('Não há caminho entre os vértices especificados.')