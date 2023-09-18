class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.previo = None

class Cola:
    def __init__(self):
        self.final = None
        self.principio = None

    def esta_vacia(self): 
        return self.final is None

    def agregarIzquierda(self, dato):
        new_node = NodoCola(dato)
        if self.final is None:
            self.final = self.principio = new_node
        else:
            new_node.siguiente = self.final
            self.final.previo = new_node
            self.final = new_node

    def agregar(self, dato):
        new_node = NodoCola(dato)
        if self.principio is None:
            self.final = self.principio = new_node
        else:
            new_node.previo = self.principio
            self.principio.siguiente= new_node
            self.principio = new_node

    def popIzquierda(self):
        if self.esta_vacia():
            return None
        dato= self.final.dato

        if self.final == self.principio:
            self.final = self.principio = None
        else:
            self.final = self.final.siguiente
            self.final.previo = None
        return dato


    def pop(self):
        if self.esta_vacia():
            return None
        dato= self.principio.dato

        if self.final == self.principio:
            self.final = self.principio = None
        else:
            self.principio = self.principio.previo
            self.principio.siguiente = None
        return dato


    def tamaño(self):
        contador = 0
        actual = self.final
        while actual:
            contador += 1
            actual = actual.siguiente

        return contador