#import module
from graphviz import Digraph

#Se inicializa la clase encargada de administrar los nodos del Grafo
class Nodo:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitando = False
        self.nivel = -1
        self.vecinos = []
    #Se crea la funcion de agregar vecinos a los nodos
    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
# Se inicializa la clase encargada de administrar las Aristas del Grafo
class Arista:
    #constructor
    def __init__(self):
        self.id = 0
    #Funcion para agregar aristas al Grafo
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)

#Se inicializa la clase Grafo que se encarga de administrar y generar los elementos del Grafo
class Grafo:
    #constructor
    def __init__(self):
        self.vertices = {}
    #Funcion para la agregación de vertices al Grafo
    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Nodo(v)
    #Función para agregar aristas al Grafo
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)
#Se inicializa clase que permite crear los archivos de visualizaciónote
#Se genera el grafo en formato GV y en formato PNG para su futuro analisis
class graphviz:
    dot = Digraph(comment='The Round Graph')
    #constructor
    def __init__(self):
        self.graphvis = {}
    #Función que agrega nodo para generar el archivo GV y PNG
    def agregaNodo(self,v):
        vs = str(v)
        self.dot.node(vs, vs)
    #Función que permite crear la lista en formato adecuado
    def listaedges(self,l2,a,b):
        c = str(a) + str(b)
        l2.append(c)
    #Función que permite agregar la lista de conexiónes
    def agregaedges(self,l2):
        self.dot.edges(l2)
    #Función encargada de generar el archivo GV como el PNG
    def imprimegrafo(self):
        print('-------Impresion y generacion GV de Grafo')
        self.dot.format = 'png'
        self.dot.render('Graphviz-output/round-table.gv', view = True)
        print(self.dot.source) #doctest: +NORMALIZE_WHITESPACE

#Función principal qcon la que se integra el GRAFO de estudio
def main():
    #Llamado de las clases
    g = Grafo()
    h = graphviz()
    #Lista de Nodos
    l = [0, 1, 2, 3, 4, 5, 6]
    for v in l:
        g.agregaVertice(v)
        h.agregaNodo(v)
    #Lista de aristas del Grafo
    l = [2, 0, 0, 6, 6, 3, 0, 5, 6, 5, 0, 1, 6, 4, 1, 4]
    l2 = []
    #Ciclo generador de aristas en pares
    for i in range(0, len(l) - 1, 2):
        a = l[i]
        b = l[i + 1]
        #agregan aristas al grafo
        g.agregarArista(a, b)
        #Se genera la lista para el archivo GV
        h.listaedges(l2,a,b)
    #se agrega lista al constructor de GV y PNG
    h.agregaedges(l2)
    #Se imprime encabezado de resultados
    print('-------Grafo lista de adyacentes')
    #Se construye la lista de adyacencia
    for v in g.vertices:
        print(v, g.vertices[v].vecinos)
    #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
    h.imprimegrafo()

main()
