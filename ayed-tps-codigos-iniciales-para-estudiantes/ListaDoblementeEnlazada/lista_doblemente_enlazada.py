from nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
    
    def __len__(self):
        return self.tamanio
    
    def esta_vacia(self):
        return self.cabeza == None
    
    def agregar_al_final(self, dato):
        if self.esta_vacia():        #si la lista esta vacia el primer nodo agredado sera el primer y cola nodo
            self.cabeza = self.cola = Nodo(dato)
        else:  # caso contrario nuestra lista ya contiene un nodos
            aux = self.cola
            self.cola = aux.siguiente = Nodo(dato)
            self.cola.anterior = aux
        self.tamanio += 1
    
    def agregar_al_inicio(self, dato):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.cabeza
            self.cabeza.anterior = aux
            self.cabeza = aux
        self.tamanio +=1

    def recorrer_inicio(self):
        aux = self.cabeza
        while aux:
            print(aux.dato)
            aux = aux.siguiente
    
    def recorrer_fin(self):
        aux = self.cola
        while aux:
            print(aux.dato)
            aux = aux.anterior
    
    def tamanio(self):
        return self.tamanio
    
    def insertar(self, dato, posicion=None ):
        aux =  Nodo(dato)
        #caso especial si la lista esta vacia
        if self.esta_vacia():
            self.cabeza = aux
            self.cola = aux
            self.tamanio +=1
            return
        #caso donde no se agregue posicion o la posicion sea mayor al tamanio de la lista
        if posicion == 0:
            aux.siguiente = self.cabeza
            self.cabeza.anterior = aux
            self.cabeza = aux
        elif posicion is None or posicion >= self.tamanio:
            aux.anterior = self.cola
            self.cola.siguiente = aux
            self.cola = aux
        else:
            actual = self.cabeza
            indice = 0

            while indice < posicion:
                actual = actual.siguiente
                indice +=1
                        
            aux.siguiente = actual
            aux.anterior = actual.anterior
            actual.anterior.siguiente = aux
            actual.anterior = aux
        self.tamanio +=1

   
    def extraer(self, posicion=None):
        if posicion is None:
            if self.tamanio == 0:
                raise IndexError("La lista está vacía, no se puede extraer ningún elemento.")
            
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            if posicion < -1 or posicion >= self.tamanio:
                raise IndexError('Indice fuera de rango.')
            
            if posicion == -1:  # Manejar la posición -1
                dato = self.cola.dato
                self.cola = self.cola.anterior
                self.cola.siguiente = None

            elif posicion == 0: # si posicion es 0
                dato = self.cabeza.dato
                self.cabeza = self.cabeza.siguiente
                if self.cabeza is not None:
                    self.cabeza.anterior = None
                else:
                    self.cola = None

            elif posicion == self.tamanio - 1: #si posicion es igual al tamanio
                dato = self.cola.dato
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            else: # caso donde busque la posicion
                actual = self.cabeza
                indice = 0
                while indice < posicion:
                    actual = actual.siguiente
                    indice += 1
                dato = actual.dato
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
        
        self.tamanio -= 1
        return dato



    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista
        
    def invertir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            temp = nodo_actual.anterior
            nodo_actual.anterior = nodo_actual.siguiente
            nodo_actual.siguiente = temp
            nodo_actual = nodo_actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza
