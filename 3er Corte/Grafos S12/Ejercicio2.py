import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        #Diccionario donde cada vertice tiene una lista de vecinos (con pesos opcionales)
        self.grafo = []
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, vertice):
        #Si el vertice no existe aun, lo agrega automaticamente con una lista vacia de vecinos
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def agregar_arista(self, u, v, peso=1):
        #Aseguramos que ambos vertices existan en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        #Agregamos la arista de u a v
        self.grafo[u].append((v, peso))
        
        #Si el grafo no es dirigido, tambien agregamos la arista de v a u
        if not self.es_dirigido:
            self.grafo[v].append((u, peso))
            
    def obtener_vecinos(self, vertice):
        #Devolvemos solo los nombtes de los vecinos ( ignoramos pesos aqui)
        if vertice in self.grafo:
            return [vecino for vecino,in self.grafo[vertice]]
        else:
            return []
    
    def existe_arista(self, u, v):
        #Verificamos si hay una arista de u a v
        if u in self.grafo:
            return any(vecino == v for vecino, in self.grafo[u])
        return False
    
    def bfs(self, inicio):
        if inicio not in self.grafo:
            print(f"Error: el vertice '{inicio}' no existe.")
            return []
        
        visitados = set()
        #Conjunto para marcar los vertices visitados
        cola = collections.deque()
        #cola para el recorrido BFS
        recorrido = []
        #Lista para almacenar el orden de visita
        
        #Comenzamos desde el vertice de inicio
        cola.append(inicio)
        visitados.add(inicio)
        
        while cola:
            actual = cola.popleft()
            #sacamos el primer vertice de la cola
            recorrido.append(actual)
            #revisamos todos los vecinos
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
            return recorrido
    def dfs(self, inicio):
        if inicio not in self.grado:
            print(f"Error: el vertice '{inicio}' no existe.")
            return []
        
        visitados = set()
        #Conjunto para marcar vertices visitados
        
        recorrido = []
        #Lista para almacenar el orden de visita
        
        
        #Funcion recursiva interna
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        
        #Iiniciamos DFS desde el vertice iniciado
        _dfs_recursivo(inicio)
        return recorrido
    
#Se crea el grafo no dirigido
grafo = Grafo(es_dirigido=False)

#Agregar aristas ( los vertices se crean automaticamente)
aristas = [('A', 'B'),('A', 'C'),('B', 'D'),('C', 'D'),('D', 'E')]
for u, v in aristas:
    grafo.agregar_arista(u, v)
    
#Agregar un vertice aislado (desconectado)
grafo.agregar_vertice('F')

#Realizar bfs y dfs desde el vertice 'A'
print("Recorrido BFS desde 'A':", grafo.bfs('A'))
print("Recorrido DFS desde 'A':", grafo.dfs('A'))

# Realizar BFS y DFS desde el vertice aislado 'F'
print("Recorrido BFS desde 'F':", grafo.bfs('F'))
print("Recorrido DFS desde 'F':", grafo.dfs('F'))