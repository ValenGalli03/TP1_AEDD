from mecla import mecla_directa
from tamano import verificar_orden_y_tamano
def main():
    archivo_entrada = 'archivo_desordenado.txt'
    archivo_salida = 'archivo_ordenado.txt'
    tamano_bloque = 10000  # Ajusto el bloque de memoria

    # Ordena el archivo
    mecla_directa(archivo_entrada, archivo_salida, tamano_bloque)

    # Verifica que el archivo resultante esté ordenado y tenga el mismo tamaño
    tamano_original, tamano_resultante = verificar_orden_y_tamano(archivo_entrada)

    if tamano_original == tamano_resultante:
        print("El archivo fue ordenado correctamente y tiene el mismo tamaño.")
    else:
        print("El archivo no fue ordenado correctamente o tiene un tamaño diferente.")

if __name__ == "__main__":
    main()
