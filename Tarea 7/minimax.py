
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

def print_board(board):
    print('-------------')
    for row in board:
        print('|', end='')
        for elem in row:
            symbol = ' ' if elem is None else elem
            print(f' {symbol} |', end='')
        print('\n-------------')


def minimax(board, depth, player):
    
    # Si se alcanzó la profundidad límite o el juego ha terminado, devolver la utilidad del tablero
    if depth == 0 or terminal_test(board)[0]:
        return utility(board, player)

    # Si es el turno del jugador, maximizar la utilidad
    if player == 'X':
        value = float('-inf')
        for action in actions(board):
            # Calcular la utilidad de cada posible acción y obtener el máximo
            value = max(value, minimax(result(board, action), depth-1, 'O'))
        return value

    # Si es el turno del oponente, minimizar la utilidad
    else:
        value = float('inf')
        for action in actions(board):
            # Calcular la utilidad de cada posible acción y obtener el mínimo
            value = min(value, minimax(result(board, action), depth-1, 'X'))
        return value
    


def actions(board):
    # Obtener las acciones posibles (posiciones vacías en el tablero)
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]


def result(board, action):
    # Realizar la acción (colocar el símbolo del jugador en la posición correspondiente)
    i, j = action
    new_board = [row.copy() for row in board]
    new_board[i][j] = 'X' if terminal_test(board)[1] == 'O' else 'O'
    return new_board

def get_best_action(board, depth, player):
    # Obtener la mejor acción para el jugador
    best_value = float('-inf')
    best_action = None
    for action in actions(board):
        # Calcular la utilidad de cada posible acción
        value = minimax(result(board, action), depth-1, player)
        
        # Si la utilidad es mayor que el mejor valor hasta el momento, actualizar el mejor valor y la mejor acción
        if value > best_value:
            best_value = value
            best_action = action

        return best_action