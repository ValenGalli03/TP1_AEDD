from lista_doblemente_enlazada import ListaDobleEnlazada

lista = ListaDobleEnlazada()

lista.agregar_al_final(2)
lista.agregar_al_inicio(1)

print('tamanio de las lista:',lista.tamanio())


print('--------recorer de inicio a fin--------')
lista.recorrer_inicio()
print('--------recorer de fin a inicio--------')
lista.recorrer_fin()
