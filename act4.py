from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

# 1. Definición del Grafo del Laberinto / Cuadrícula
def crear_laberinto():
    G = nx.Graph()
    # Definimos las conexiones (pasillos) del laberinto
    conexiones = [
        ('Inicio', 'A1'), ('Inicio', 'B1'),
        ('A1', 'A2'), ('B1', 'C1'),
        ('A2', 'Meta'), ('C1', 'C2'), ('C2', 'Meta'),
        ('B1', 'B2') # Ruta alterna más larga
    ]
    G.add_edges_from(conexiones)
    return G

# 2. Algoritmo BFS (Búsqueda en Anchura)
def busqueda_bfs(grafo, inicio, meta):
    cola = deque([[inicio]])
    visitados = {inicio}
    nodos_expandidos = 0
    
    while cola:
        camino = cola.popleft()
        nodo = camino[-1]
        nodos_expandidos += 1
        
        if nodo == meta:
            return camino, nodos_expandidos
            
        for vecino in grafo.neighbors(nodo):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return None, nodos_expandidos

# 3. Algoritmo DFS (Búsqueda en Profundidad)
def busqueda_dfs(grafo, inicio, meta):
    pila = [[inicio]]
    visitados = set()
    nodos_expandidos = 0
    
    while pila:
        camino = pila.pop()
        nodo = camino[-1]
        
        if nodo not in visitados:
            visitados.add(nodo)
            nodos_expandidos += 1
            
            if nodo == meta:
                return camino, nodos_expandidos
                
            for vecino in reversed(list(grafo.neighbors(nodo))):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    pila.append(nuevo_camino)
    return None, nodos_expandidos

# --- EJECUCIÓN Y VISUALIZACIÓN ---
if __name__ == "__main__":
    G = crear_laberinto()
    inicio = 'Inicio'
    meta = 'Meta'
    
    camino_bfs, exp_bfs = busqueda_bfs(G, inicio, meta)
    camino_dfs, exp_dfs = busqueda_dfs(G, inicio, meta)
    
    print(f"BFS -> Camino: {camino_bfs} | Nodos expandidos: {exp_bfs}")
    print(f"DFS -> Camino: {camino_dfs} | Nodos expandidos: {exp_dfs}")
    
    # Graficar la red con Matplotlib
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray', width=2)
    
    # Destacar camino BFS en verde
    edges_bfs = list(zip(camino_bfs[:-1], camino_bfs[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges_bfs, edge_color='green', width=4)
    
    plt.title("Comparativa de Búsqueda Ciega en Grafo (BFS en Verde)")
    plt.show()