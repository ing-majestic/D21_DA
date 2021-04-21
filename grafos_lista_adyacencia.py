class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitando = False
        self.nivel = -1
        self.vecinos = []

    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)


def main():
    g = Grafica()


    l = [0, 1, 2, 3, 4, 5, 6]
    for v in l:
        g.agregaVertice(v)

    l = [2, 0, 0, 6, 6, 3, 0, 5, 6, 5, 0, 1, 6, 4, 1, 4]
    for i in range(0, len(l) - 1, 2):
        g.agregarArista(l [i], l [i + 1])

    for v in g.vertices:
        print(v, g.vertices[v].vecinos)

main()
