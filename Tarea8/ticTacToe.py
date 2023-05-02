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


def minimax(board, depth, player, alpha, beta):
    if depth == 0 or terminal_test(board)[0]:
        return utility(board, player)

    if player == 'X':
        value = float('-inf')
        for action in actions(board):
            result_board = result(board, action)
            value = max(value, minimax(result_board, depth-1, 'O', alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for action in actions(board):
            result_board = result(board, action)
            value = min(value, minimax(result_board, depth-1, 'X', alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
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
    best_value = float('-inf')
    best_action = None
    alpha = float('-inf')
    beta = float('inf')
    for action in actions(board):
        result_board = result(board, action)
        value = minimax(result_board, depth-1, player, alpha, beta)
        if value > best_value:
            best_value = value
            best_action = action
        alpha = max(alpha, best_value)
    return best_action