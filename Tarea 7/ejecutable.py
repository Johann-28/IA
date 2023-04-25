import minimax as mm

board = [
    ['X','X','O'],
    [None,'O',None],
    [None,None,None]
]

depth = 5
player = 'X'

best_value = mm.minimax(board, depth, player)
best_action = mm.get_best_action(board, depth, player)

print(f"El mejor valor para el jugador {player} es: {best_value}")
print(f"La mejor acción para el jugador {player} es: {best_action}")