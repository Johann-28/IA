import random
from ticTacToe import *

# Definir la función para dibujar el tablero
def draw_board(board):
    print('-------------')
    for row in board:
        print('|', end='')
        for cell in row:
            symbol = ' ' if cell is None else cell
            print(f' {symbol} |', end='')
        print('\n-------------')

def terminal_test(board):
    # Comprobar si hay alguna fila con tres elementos iguales
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return True, row[0]
    
    # Comprobar si hay alguna columna con tres elementos iguales
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return True, board[0][col]
    
    # Comprobar si hay alguna diagonal con tres elementos iguales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return True, board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return True, board[0][2]
    
    # Comprobar si el tablero está lleno (empate)
    if all([all(row) for row in board]):
        return True, None
    
    # Si no hay ganador y el tablero no está lleno, el juego no ha terminado
    return False, None


def utility(board, player):
    # Obtener el ganador del tablero
    is_terminal, winner = terminal_test(board)
    
    # Si el ganador es el jugador, la utilidad es 1
    if winner == player:
        return 1
    # Si el tablero está lleno y no hay ganador, la utilidad es 0 (empate)
    elif winner is None:
        return 0
    # Si el ganador es el oponente, la utilidad es -1
    else:
        return -1

# Definir la función para que el jugador haga una jugada
def player_move(board):
    while True:
        try:
            row = int(input('Elige una fila (0, 1, 2): '))
            col = int(input('Elige una columna (0, 1, 2): '))
            if board[row][col] is not None:
                print('Esa posición ya está ocupada. Inténtalo de nuevo.')
            else:
                board[row][col] = 'X'
                break
        except (ValueError, IndexError):
            print('Entrada inválida. Inténtalo de nuevo.')

# Definir la función para que la computadora haga una jugada
def computer_move(board, depth):
    print('La computadora está pensando...')
    bestAction = get_best_action(board, depth, 'O')
    board[bestAction[0]][bestAction[1]] = 'O'
    print(f'La computadora ha colocado una pieza en la fila {bestAction[0]}, columna {bestAction[1]}.')

# Crear el tablero vacío
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Mostrar el tablero vacío
draw_board(board)

# Jugar hasta que haya un ganador o empate
while not terminal_test(board)[0]:
    # Jugada del jugador
    player_move(board)
    draw_board(board)
    if terminal_test(board)[0]:
        break
    
    # Jugada de la computadora
    computer_move(board, depth=6)
    draw_board(board)

# Mostrar el resultado del juego
winner = terminal_test(board)[1]
if winner is None:
    print('¡Empate!')
else:
    print(f'¡{winner} ha ganado!')
