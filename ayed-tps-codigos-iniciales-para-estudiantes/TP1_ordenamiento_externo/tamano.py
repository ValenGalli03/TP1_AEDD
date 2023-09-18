def obtener_tamano_archivo(nombre_archivo):
    tamano = 0
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            tamano += len(linea)
    return tamano

def verificar_orden_y_tamano(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    if all(int(lineas[i]) <= int(lineas[i+1]) for i in range(len(lineas)-1)):
        print("El archivo está ordenado correctamente.")
    else:
        print("El archivo no está ordenado correctamente.")

    tamano_original = obtener_tamano_archivo('archivo_desordenado.txt')
    tamano_resultante = obtener_tamano_archivo('archivo_ordenado.txt')

    return tamano_original, tamano_resultante