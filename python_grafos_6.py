class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conect_A = {}
    def agregarVecino(self,proximo,ponderacion=0):
        self.conect_A[proximo] = ponderacion

    def __str__(self):
        return str(self.id) + ' conect_A: ' + str([x.id for x in self.conect_A])

    def obtenerConexiones(self):
        return self.conect_A.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,proximo):
        return self.conect_A[vecino]

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
g = Grafo()
