
#Se importaran nuevas caracteristicas de print

from __future__ import  print_function

#Se crea la clace vertice que solo tiene como argumento su nombre

class Vertice(object):
    def __init__(self, n):
        self.nombre = n

#Se crea la clase grafo con vertices e indices de bordes como diccionarios
#y tambien los bordes como listaVertices
class Grafo(object):
    vertices = {}
    bordes = []
    indices_bordes = {}

    def agregarVertice(self, vertice):
        #se agrega ,si vertice es una instancia de su clase y su nombre no esta, en el diciconario de vertices
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            #Se recorre los bordes y se agrega
            for fila in self.bordes:
                fila.append(0)
            self.bordes.append([0] * (len(self.bordes)+1))
            self.indices_bordes[vertice.nombre] = len(self.indices_bordes)
            return True
        else:
            return False
    def agregarBorde(self, u, v, peso=1):
        #se agrega el borde
        if u in self.vertices and v in self.vertices:
            self.bordes[self.indices_bordes[u]][self.indices_bordes[v]] = peso
            self.bordes[self.indices_bordes[v]][self.indices_bordes[u]] = peso
            return True
        else:
            return False

    def printGrafo(self):
        #se muestra el Grafo
        for v, i in sorted(self.indices_bordes.items()):
            print(v + ' ', end='')
            for j in range(len(self.bordes)):
                print(self.bordes[i][j], end='')
            print('')

if __name__ == '__main__':
    g = Grafo()

    cinco = Vertice('5')
    tres = Vertice('3')
    cuatro = Vertice('4')
    uno = Vertice('1')
    dos = Vertice('2')

    for i in range(ord('1'), ord('6')):
        g.agregarVertice(Vertice(chr(i)))

    bordes = ['53', '54', '31', '35', '41', '42', '45', '12', '13', '14', '21', '24']

    for borde in bordes:
        g.agregarBorde(borde[:1],borde[1:])

g.printGrafo()
