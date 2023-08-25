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

    def insertar(self, dato, posicion=None ):
        aux =  Nodo(dato)
        #caso especial si la lista esta vacia
        if self.esta_vacia():
            self.primero = aux
            self.ultimo = aux
            return
        #caso donde no se agregue posicion o la posicion sea mayor al tamanio de la lista
        elif posicion is None or posicion >= self.size:
            aux.anterior = self.ultimo
            self.ultimo.siguiente = aux
            self.ultimo = aux
        else:
            actual = self.primero
            indice = 0

            while indice < posicion:
                actual = actual.siguiente
                indice +=1
                           
            aux.siguiente = actual
            aux.anterior = actual.anterior
            actual.anterior.siguiente = aux
            actual.anterior = aux
        self.size +=1
        
    def extraer(self, posicion):
        
        if posicion < 0 or posicion >= self.tamanio():
            raise IndexError('Indice fuera de rango.')
        
        if posicion == 0: #Evaluo el caso donde la posicion es 0 
            dato = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero is not None:
                self.primero.anterior = None
            else:
                self.ultimo = None

        elif posicion == self.tamanio()-1: # Evaluo si la posicion es la ultima
            dato = self.ultimo.dato
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            
        else:
            actual = self.primero
            indice = 0
            while indice < posicion:
                actual = actual.siguiente
                indice += 1
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self.size -= 1
        return dato
        
    def copiar(self):
        copia_lista = ListaDoblementeEnlazada()
        actual = self.primero
        
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista.recorrer_inicio()
