from nodo import Nodo

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def esta_vacia(self):
        return self.primero == None
    
    def agregar_al_final(self, dato):
        if self.esta_vacia():        #si la lista esta vacia el primer nodo agredado sera el primer y ultimo nodo
            self.primero = self.ultimo = Nodo(dato)
        else:  # caso contrario nuestra lista ya contiene un nodos
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
    
    def agregar_al_inicio(self, dato):
        if self.esta_vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.size +=1

    def recorrer_inicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
    
    def recorrer_fin(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
    
    def tamanio(self):
        return self.size

    def insertar(self, dato, posicion):
        aux =  Nodo(dato)
        #caso especial si la lista esta vacia
        if self.esta_vacia():
            self.primero = aux
            self.ultimo = aux
            return
        
        actual = self.primero
        indice = 0
        while actual is not None and indice < posicion:
            actual = actual.siguiente
            indice +=1
        if actual is None:
            # Si la posición excede el tamaño de la lista, agregamos al final
            aux.anterior = self.ultimo
            self.ultimo.siguiente = aux
            self.ultimo = aux
        else:
            aux.siguiente = actual
            aux.anterior = actual.anterior
            actual.anterior.siguiente = aux
            actual.anterior = aux
