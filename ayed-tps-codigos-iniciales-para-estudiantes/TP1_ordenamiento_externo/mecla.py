def mecla_directa(archivo_entrada, archivo_salida, tamano_bloque):
    # Abre el archivo de entrada en modo lectura
    with open(archivo_entrada, 'r') as archivo_entrada:
        lineas = archivo_entrada.readlines()
    
    # Divide las líneas en bloques y ordena cada bloque
    for i in range(0, len(lineas), tamano_bloque):
        bloque = lineas[i:i + tamano_bloque]
        bloque.sort()
        with open(f'tmp_{i}.txt', 'w') as archivo_temporal:
            archivo_temporal.writelines(bloque)
    
    # Mezcla los bloques ordenados
    with open(archivo_salida, 'w') as archivo_salida:
        archivos_temporales = [open(f'tmp_{i}.txt', 'r') for i in range(0, len(lineas), tamano_bloque)]
        valores = [int(archivo_temp.readline()) for archivo_temp in archivos_temporales]
        while any(valores):
            indice_min = min((valor, i) for i, valor in enumerate(valores) if valor is not None)[1]
            archivo_salida.write(str(valores[indice_min]) + '\n')
            linea = archivos_temporales[indice_min].readline()
            if linea:
                valores[indice_min] = int(linea)
            else:
                valores[indice_min] = None
                archivos_temporales[indice_min].close()