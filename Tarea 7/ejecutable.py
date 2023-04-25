import minimax as mm
import time

board = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]

depth = 1000
player = 'X'

while not mm.terminal_test(board)[0]:
    print("Es el turno del jugador", player)
    print("Tablero actual:")
    mm.print_board(board)
    
    row = int(input("Ingresa el número de fila (0, 1, 2): "))
    while not 0 <= row <= 2:
        row = int(input("Rango incorrecto. Ingresa de nuevo el número de fila (0, 1, 2): "))
       
       
    col = int(input("Ingresa el número de columna (0, 1, 2): "))
    while not 0 <= col <= 2:
        col = int(input("Rango incorrecto. Ingresa de nuevo el número de columna (0, 1, 2): "))

   
     
    if board[row][col] is not None:
        print("Esa casilla ya está ocupada. Intenta de nuevo.")
        continue
    board[row][col] = player
    mm.print_board(board)
    if mm.terminal_test(board)[0]:
        break
    
    print("Pensando.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    
    
    inicio = time.time()
    best_action = mm.get_best_action(board, depth, 'O')
    board = mm.result(board, best_action)
    fin = time.time()
    
    print("La máquina ha jugado:")
    print("Tiempo destinado" , fin - inicio)
    mm.print_board(board)
    player = 'X' if player == 'O' else 'X'

print("Juego terminado.")
if mm.terminal_test(board)[1] is None:
    print("¡Empate!")
else:
    print("Ha ganado el jugador", mm.terminal_test(board)[1])
