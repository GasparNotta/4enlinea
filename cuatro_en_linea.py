from typing import List

SIMBOLO_1 = 'X'
SIMBOLO_2 = 'O'

def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """
    Crea un tablero vacío con el número especificado de filas y columnas.

    Args:
        n_filas (int): Número de filas en el tablero.
        n_columnas (int): Número de columnas en el tablero.

    Returns:
        List[List[str]]: El tablero recién creado.
    """
    tablero = [[' ' for _ in range(n_columnas)] for _ in range(n_filas)]
    return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """
    Determina si es el turno del jugador con el símbolo X.

    Args:
        tablero (List[List[str]]): El tablero del juego.

    Returns:
        bool: True si es el turno del jugador con el símbolo X, False de lo contrario.
    """
    cantidad_de_simbolo_1 = sum(fila.count(SIMBOLO_1) for fila in tablero)
    cantidad_de_simbolo_2 = sum(fila.count(SIMBOLO_2) for fila in tablero)

    return cantidad_de_simbolo_1 == cantidad_de_simbolo_2

def tablero_completo(tablero: List[List[str]]) -> bool:
    """
    Verifica si el tablero está completo (no hay espacios vacíos).

    Args:
        tablero (List[List[str]]): El tablero del juego.

    Returns:
        bool: True si el tablero está completo, False de lo contrario.
    """
    return all(cell != ' ' for row in tablero for cell in row)

def obtener_ganador(tablero: List[List[str]]) -> str:
    """
    Determina si hay un ganador en el juego Cuatro en Línea.

    Args:
        tablero (List[List[str]]): El tablero del juego.

    Returns:
        str: El símbolo del jugador ganador ('X', 'O') o un espacio si no hay ganador.
    """
    for fila in tablero:
        fila_texto = ''.join(fila)
        if SIMBOLO_1*4 in fila_texto:
            return SIMBOLO_1
        elif SIMBOLO_2*4 in fila_texto:
            return SIMBOLO_2
        
    for columna in range(len(tablero[0])):
        columna_texto = ''.join(tablero[fila][columna] for fila in range(len(tablero)))
        if SIMBOLO_1*4 in columna_texto:
            return SIMBOLO_1
        elif SIMBOLO_2*4 in columna_texto:
            return SIMBOLO_2

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] == ' ':
                continue
            else:
                if fila - 3 >= 0 and columna + 3 < len(tablero[0]) and all(tablero[fila - k][columna + k] == tablero[fila][columna] for k in range(4)):
                    return tablero[fila][columna]
                if fila + 3 < len(tablero) and columna + 3 < len(tablero[0]) and all(tablero[fila + k][columna + k] == tablero[fila][columna] for k in range(4)):
                    return tablero[fila][columna]

    return ' '