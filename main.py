import cuatro_en_linea
from typing import List

SALIDA = 's'

def mensaje_en_consola(mensaje: str) -> None:
    """
    Muestra un mensaje en la consola con un formato específico.

    Args:
        mensaje (str): El mensaje que se va a mostrar.
    """
    print(f'-----------------------------------\n{mensaje}\n-----------------------------------')

def pedir_columna(columna: str, columnas_totales: int) -> None:
    """
    Verifica si la columna ingresada es un número válido.

    Args:
        columna (str): La columna ingresada por el usuario.
        columnas_totales (int): El número total de columnas en el tablero.
    """
    if not columna.isdigit():
        mensaje_en_consola('La columna debe ser un número.')
    elif not 0 <= int(columna) < columnas_totales:
        mensaje_en_consola(f'La columna ingresada debe estar entre 0 y {columnas_totales - 1}.')

def dibujo_de_tablero(tablero: List[List[str]]) -> None:
    """
    Dibuja el tablero en la consola.

    Args:
        tablero (List[List[str]]): El tablero del juego.
    """
    for n, fila in enumerate(tablero):
        if n == 0:
            print('|', end='')
            for k in range(len(tablero[0])):
                print(f' {k} |', end='')
            print()
            print(('_' * (len(tablero[0]) * 4)) + '_')
            print()
        else:
            print()
        for i, celda in enumerate(fila):
            if i == 0:
                print('|', end='')
            print(f' {celda} |', end='')
    print()

def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """
    Inserta el símbolo correspondiente en la columna indicada.

    Args:
        tablero (List[List[str]]): El tablero del juego.
        columna (int): El número de columna donde se insertará el símbolo.

    Returns:
        bool: True si la inserción fue exitosa, False si la columna está llena.
    """
    if not 0 <= columna < len(tablero[0]):
        print('La columna ingresada no es válida')
        return False
    
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == ' ':
            simbolo = cuatro_en_linea.SIMBOLO_1 if cuatro_en_linea.es_turno_de_x(tablero) else cuatro_en_linea.SIMBOLO_2
            tablero[fila][columna] = simbolo
            return True

    print('La columna ingresada está llena')
    return False

def main() -> None:
    """
    Función principal para ejecutar el juego Cuatro en Línea.
    """
    verificador = False
    while not verificador:
        print('------------4 EN LINEA------------')
        posible_fila = input('Ingrese el ancho del juego entre 4 y 10: ')
        posible_columna = input('Ingrese el alto del juego entre 4 y 10: ')
        print('-----------------------------------')
        try:
            filas = int(posible_fila)
            columnas = int(posible_columna)

            if not (4 <= filas <= 10) or not (4 <= columnas <= 10):
                print('El número de filas y columnas deben estar entre 4 y 10. Inténtelo de nuevo.\n')
            else:
                verificador = True
                tablero = cuatro_en_linea.crear_tablero(filas, columnas)
        except ValueError:
            print('El número de filas o columnas debe ser un número entero. Inténtelo de nuevo.\n')

    while True:
        dibujo_de_tablero(tablero)

        if cuatro_en_linea.es_turno_de_x(tablero):
            simbolo = 'X'
        else:
            simbolo = 'O'
        columna_ingresada = input(f'Ingrese la columna deseada para insertar {simbolo} entre 0 y {columnas - 1} o ingrese la letra s para salir: ')
        
        if columna_ingresada.lower() == SALIDA:
            break
        
        pedir_columna(columna_ingresada, columnas)
        insertar_simbolo(tablero, int(columna_ingresada))

        if cuatro_en_linea.tablero_completo(tablero):
            mensaje_en_consola('El juego terminó porque se llenó el tablero. Empate')
            break

        ganador = cuatro_en_linea.obtener_ganador(tablero)
        if ganador == cuatro_en_linea.SIMBOLO_1 or ganador == cuatro_en_linea.SIMBOLO_2:
            dibujo_de_tablero(tablero)
            mensaje_en_consola(f'El ganador es {ganador}')
            break

        


 
main()