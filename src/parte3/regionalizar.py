def regionalizar(tablero, tam, fila_silo, col_silo, fila_inicio, col_inicio, region=1):
    # Paso 1 Caso base: Pinta las tres celdas que no son silo (-1) o falso silo (-2). Dejando una region en forma de L
    if tam == 2:
        for i in range(2):
            for j in range(2):
                if tablero[fila_inicio + i][col_inicio + j] == 0:
                    tablero[fila_inicio + i][col_inicio + j] = region
        return region + 1

    # Paso 2: Identificar posicion de L y pintar silos falsos
    medio = tam // 2
    silo_cuadrante = (2 if fila_silo >= fila_inicio + medio else 0) + (1 if col_silo >= col_inicio + medio else 0)
    pintar_silos_falsos(tablero, medio, fila_inicio, col_inicio, silo_cuadrante)

    imprimir_tablero(tablero)
    # Paso 3: Dividir subproblemas en 4 y resolverlos recursivamente
    nueva_region = region
    for i in range(2):
        for j in range(2):
            nuevo_fila_inicio = fila_inicio + i * medio
            nuevo_col_inicio = col_inicio + j * medio
            if nuevo_fila_inicio <= fila_silo < nuevo_fila_inicio + medio and nuevo_col_inicio <= col_silo < nuevo_col_inicio + medio:
                # Silo real en este subcuadrante
                nueva_region = regionalizar(tablero, medio, fila_silo, col_silo, nuevo_fila_inicio, nuevo_col_inicio,
                                            nueva_region)
            else:
                # No hay silo real, revisar para silo virtual
                nueva_region = regionalizar(tablero, medio, fila_inicio + medio // 2, col_inicio + medio // 2,
                                            nuevo_fila_inicio, nuevo_col_inicio, nueva_region)
    for i in range(fila_inicio + medio - 1, fila_inicio + medio + 1):
        for j in range(col_inicio + medio - 1, col_inicio + medio + 1):
            if tablero[i][j] == -2:
                tablero[i][j] = nueva_region
    return nueva_region + 1


def pintar_silos_falsos(tablero, medio, fila_inicio, col_inicio, silo_cuadrante):
    if silo_cuadrante == 0:  # Silo real en cuadrante superior izquierdo
        tablero[fila_inicio + medio - 1][col_inicio + medio] = -2  # Superior derecho
        tablero[fila_inicio + medio][col_inicio + medio - 1] = -2  # Inferior izquierdo
        tablero[fila_inicio + medio][col_inicio + medio] = -2  # Inferior derecho
    elif silo_cuadrante == 1:  # Silo real en cuadrante superior derecho
        tablero[fila_inicio + medio - 1][col_inicio + medio - 1] = -2  # Superior izquierdo
        tablero[fila_inicio + medio][col_inicio + medio] = -2  # Inferior derecho
        tablero[fila_inicio + medio][col_inicio + medio - 1] = -2  # Inferior izquierdo
    elif silo_cuadrante == 2:  # Silo real en cuadrante inferior izquierdo
        tablero[fila_inicio + medio - 1][col_inicio + medio - 1] = -2  # Superior izquierdo
        tablero[fila_inicio + medio - 1][col_inicio + medio] = -2  # Superior derecho
        tablero[fila_inicio + medio][col_inicio + medio] = -2  # Inferior derecho
    elif silo_cuadrante == 3:  # Silo real en cuadrante inferior derecho
        tablero[fila_inicio + medio - 1][col_inicio + medio - 1] = -2  # Superior izquierdo
        tablero[fila_inicio + medio][col_inicio + medio - 1] = -2  # Inferior izquierdo
        tablero[fila_inicio + medio - 1][col_inicio + medio] = -2  # Superior derecho


def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(str(x) if x != 0 else '-' for x in fila))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Uso: python regionalizar.py n fila_silo col_silo")
        sys.exit()

    n = int(sys.argv[1])
    fila_silo = int(sys.argv[2])  # Ajuste para índice basado en cero
    col_silo = int(sys.argv[3])

    tablero = [[0 for _ in range(n)] for _ in range(n)]
    tablero[fila_silo][col_silo] = -1
    regionalizar(tablero, n, fila_silo, col_silo, 0, 0)
    imprimir_tablero(tablero)
