import grafo as gr
grafica = {
    0: [(1, 1), (9, 8), (11, 5), (12, 2), (16, 2), (17, 5), (18, 10), (19, 5), (21, 7), (23, 8), (25, 8), (26, 1), (28, 7), (31, 4), (33, 8), (35, 1), (36, 2), (39, 7), (45, 6), (46, 7), (47, 2)],
    1: [(0, 1), (4, 3), (5, 3), (7, 7), (8, 10), (10, 5), (11, 1), (13, 1), (14, 9), (16, 7), (17, 5), (19, 9), (21, 2), (22, 3), (28, 8), (29, 1), (30, 5), (32, 7), (34, 1), (35, 9), (36, 7), (41, 1), (44, 6), (45, 6), (46, 10), (48, 3), (49, 8)],
    2: [(6, 9), (7, 4), (9, 5), (11, 4), (14, 8), (15, 7), (19, 2), (22, 7), (26, 1), (27, 1), (28, 7), (29, 9), (31, 2), (32, 1), (34, 9), (35, 6), (38, 2), (41, 1), (44, 4), (46, 2), (48, 3)],
    3: [(4, 9), (5, 4), (6, 2), (8, 3), (12, 3), (13, 1), (14, 10), (15, 7), (16, 2), (18, 4), (19, 8), (20, 1), (21, 1), (24, 9), (26, 3), (28, 2), (29, 2), (32, 5), (33, 7), (35, 9), (36, 3), (37, 2), (38, 4), (41, 6), (42, 2), (43, 2), (44, 10), (46, 7), (48, 2), (49, 10)],
    4: [(1, 3), (3, 9), (8, 9), (10, 2), (11, 5), (13, 7), (14, 1), (16, 7), (17, 6), (19, 3), (23, 1), (24, 3), (25, 1), (27, 6), (29, 8), (32, 8), (33, 4), (36, 10), (38, 8), (39, 3), (46, 10), (49, 6)],
    5: [(1, 3), (3, 4), (7, 1), (8, 7), (10, 7), (12, 10), (14, 10), (15, 8), (16, 2), (17, 2), (19, 3), (21, 2), (24, 10), (25, 10), (26, 9), (27, 4), (28, 6), (29, 2), (30, 1), (31, 9), (33, 9), (34, 1), (35, 8), (37, 10), (40, 4), (44, 10), (48, 7)],
    6: [(2, 9), (3, 2), (7, 10), (8, 9), (10, 7), (12, 6), (17, 4), (19, 8), (23, 5), (32, 10), (33, 9), (34, 2), (38, 8), (41, 7), (42, 9), (43, 7), (47, 7), (48, 10)],
    7: [(1, 7), (2, 4), (5, 1), (6, 10), (8, 1), (9, 7), (10, 7), (11, 6), (12, 4), (14, 3), (15, 1), (19, 8), (20, 3), (21, 2), (23, 8), (24, 1), (25, 3), (26, 3), (27, 9), (28, 7), (29, 8), (30, 4), (31, 2), (33, 8), (34, 2), (36, 1), (38, 8), (39, 1), (40, 2), (41, 6), (43, 5), (44, 3), (45, 8), (46, 2)],
    8: [(1, 10), (3, 3), (4, 9), (5, 7), (6, 9), (7, 1), (10, 2), (19, 10), (20, 3), (22, 7), (23, 8), (24, 3), (25, 2), (28, 8), (29, 6), (30, 10), (33, 3), (34, 1), (36, 7), (39, 6), (40, 4), (42, 4), (43, 5), (44, 10), (45, 4), (46, 10), (47, 8)],
    9: [(0, 8), (2, 5), (7, 7), (10, 2), (14, 7), (17, 3), (18, 9), (21, 9), (22, 10), (24, 2), (25, 7), (29, 7), (31, 10), (33, 2), (35, 4), (36, 1), (37, 5), (39, 4), (40, 2), (44, 2), (45, 6), (46, 8), (48, 7), (49, 9)],
    10: [(1, 5), (4, 2), (5, 7), (6, 7), (7, 7), (8, 2), (9, 2), (11, 7), (12, 3), (15, 3), (17, 6), (19, 7), (22, 3), (23, 10), (24, 10), (27, 2), (29, 5), (30, 10), (31, 9), (32, 8), (43, 8), (47, 2), (48, 6)],
    11: [(0, 5), (1, 1), (2, 4), (4, 5), (7, 6), (10, 7), (12, 9), (13, 9), (17, 1), (19, 10), (20, 4), (23, 10), (25, 3), (26, 6), (27, 1), (28, 2), (36, 6), (41, 1), (43, 9), (45, 1), (49, 7)],
    12: [(0, 2), (3, 3), (5, 10), (6, 6), (7, 4), (10, 3), (11, 9), (13, 10), (15, 7), (16, 8), (17, 8), (18, 6), (19, 4), (22, 1), (25, 2), (26, 10), (28, 6), (30, 8), (31, 7), (32, 6), (33, 1), (34, 7), (35, 7), (37, 9), (38, 10), (40, 9), (45, 10), (47, 5)],
    13: [(1, 1), (3, 1), (4, 7), (11, 9), (12, 10), (16, 3), (17, 2), (22, 6), (23, 3), (26, 5), (27, 7), (29, 2), (31, 2), (32, 9), (33, 8), (35, 6), (36, 1), (38, 2), (40, 5), (41, 7), (42, 3), (44, 1), (45, 4)],
    14: [(1, 9), (2, 8), (3, 10), (4, 1), (5, 10), (7, 3), (9, 7), (17, 8), (18, 5), (23, 3), (25, 7), (35, 1), (38, 4), (44, 8), (46, 7), (49, 1)],
    15: [(2, 7), (3, 7), (5, 8), (7, 1), (10, 3), (12, 7), (17, 1), (18, 2), (19, 4), (22, 4), (23, 4), (24, 2), (25, 7), (27, 7), (28, 4), (29, 5), (34, 6), (36, 8), (41, 9), (42, 8), (43, 10), (45, 5), (48, 1)],
    16: [(0, 2), (1, 7), (3, 2), (4, 7), (5, 2), (12, 8), (13, 3), (21, 10), (22, 6), (24, 4), (26, 5), (28, 3), (29, 4), (30, 4), (31, 8), (33, 3), (34, 10), (35, 6), (36, 3), (39, 4), (40, 2), (41, 1), (44, 7), (46, 2), (47, 4), (48, 8), (49, 6)],
    17: [(0, 5), (1, 5), (4, 6), (5, 2), (6, 4), (9, 3), (10, 6), (11, 1), (12, 8), (13, 2), (14, 8), (15, 1), (18, 3), (19, 4), (26, 9), (31, 1), (35, 9), (40, 10), (42, 9), (44, 5), (45, 2), (46, 10)],
    18: [(0, 10), (3, 4), (9, 9), (12, 6), (14, 5), (15, 2), (17, 3), (20, 10), (21, 1), (26, 5), (27, 4), (28, 2), (35, 10), (39, 9), (40, 5), (41, 8), (47, 9), (48, 8)],
    19: [(0, 5), (1, 9), (2, 2), (3, 8), (4, 3), (5, 3), (6, 8), (7, 8), (8, 10), (10, 7), (11, 10), (12, 4), (15, 4), (17, 4), (21, 9), (25, 3), (26, 5), (27, 8), (29, 2), (30, 3), (31, 10), (32, 6), (33, 9), (34, 6), (36, 6), (38, 7), (39, 4), (44, 4), (45, 2), (46, 6), (47, 7), (48, 10)],
    20: [(3, 1), (7, 3), (8, 3), (11, 4), (18, 10), (21, 9), (22, 8), (23, 8), (27, 5), (30, 1), (31, 7), (32, 10), (34, 6), (36, 5), (39, 5), (40, 5), (42, 8), (45, 8)],
    21: [(0, 7), (1, 2), (3, 1), (5, 2), (7, 2), (9, 9), (16, 10), (18, 1), (19, 9), (20, 9), (22, 4), (23, 7), (25, 2), (27, 8), (29, 3), (32, 8), (33, 1), (34, 2), (36, 10), (37, 6), (40, 7), (41, 4), (42, 1), (44, 1), (45, 2), (46, 3), (47, 9), (49, 4)],
    22: [(1, 3), (2, 7), (8, 7), (9, 10), (10, 3), (12, 1), (13, 6), (15, 4), (16, 6), (20, 8), (21, 4), (24, 7), (25, 4), (26, 4), (29, 5), (30, 7), (31, 7), (32, 3), (33, 5), (35, 8), (38, 4), (39, 1), (40, 1), (42, 10), (44, 7), (45, 9), (47, 10), (48, 10), (49, 7)],
    23: [(0, 8), (4, 1), (6, 5), (7, 8), (8, 8), (10, 10), (11, 10), (13, 3), (14, 3), (15, 4), (20, 8), (21, 7), (25, 9), (35, 2), (40, 6), (41, 6), (42, 2), (43, 9), (44, 3), (45, 1), (47, 9), (48, 10), (49, 8)],
    24: [(3, 9), (4, 3), (5, 10), (7, 1), (8, 3), (9, 2), (10, 10), (15, 2), (16, 4), (22, 7), (25, 3), (31, 8), (33, 6), (34, 5), (35, 6), (37, 3), (39, 9), (40, 2), (45, 10), (47, 9)],
    25: [(0, 8), (4, 1), (5, 10), (7, 3), (8, 2), (9, 7), (11, 3), (12, 2), (14, 7), (15, 7), (19, 3), (21, 2), (22, 4), (23, 9), (24, 3), (27, 2), (28, 1), (29, 1), (31, 1), (32, 3), (34, 5), (40, 9), (43, 4), (45, 2), (46, 7), (47, 6), (49, 6)],
    26: [(0, 1), (2, 1), (3, 3), (5, 9), (7, 3), (11, 6), (12, 10), (13, 5), (16, 5), (17, 9), (18, 5), (19, 5), (22, 4), (28, 7), (30, 2), (33, 7), (36, 7), (37, 9), (38, 4), (39, 3), (40, 7), (42, 9), (44, 2), (47, 4), (48, 2)],
    27: [(2, 1), (4, 6), (5, 4), (7, 9), (10, 2), (11, 1), (13, 7), (15, 7), (18, 4), (19, 8), (20, 5), (21, 8), (25, 2), (29, 9), (30, 1), (32, 8), (34, 8), (37, 3), (39, 4), (43, 3), (46, 4), (47, 1), (49, 6)],
    28: [(0, 7), (1, 8), (2, 7), (3, 2), (5, 6), (7, 7), (8, 8), (11, 2), (12, 6), (15, 4), (16, 3), (18, 2), (25, 1), (26, 7), (29, 2), (31, 10), (32, 5), (35, 3), (37, 7), (38, 2), (40, 6), (42, 8), (44, 8), (47, 9), (49, 10)],
    29: [(1, 1), (2, 9), (3, 2), (4, 8), (5, 2), (7, 8), (8, 6), (9, 7), (10, 5), (13, 2), (15, 5), (16, 4), (19, 2), (21, 3), (22, 5), (25, 1), (27, 9), (28, 2), (30, 1), (37, 3), (39, 2), (40, 1), (41, 3), (43, 6), (45, 6), (47, 10), (48, 1)],
    30: [(1, 5), (5, 1), (7, 4), (8, 10), (10, 10), (12, 8), (16, 4), (19, 3), (20, 1), (22, 7), (26, 2), (27, 1), (29, 1), (33, 9), (40, 3), (41, 6), (43, 4), (44, 3)],
    31: [(0, 4), (2, 2), (5, 9), (7, 2), (9, 10), (10, 9), (12, 7), (13, 2), (16, 8), (17, 1), (19, 10), (20, 7), (22, 7), (24, 8), (25, 1), (28, 10), (32, 6), (34, 1), (35, 3), (37, 6), (38, 6), (39, 5), (41, 7), (43, 5), (44, 10), (45, 7), (47, 7), (49, 8)],
    32: [(1, 7), (2, 1), (3, 5), (4, 8), (6, 10), (10, 8), (12, 6), (13, 9), (19, 6), (20, 10), (21, 8), (22, 3), (25, 3), (27, 8), (28, 5), (31, 6), (35, 9), (36, 7), (37, 4), (38, 1), (42, 2), (47, 7), (49, 6)],
    33: [(0, 8), (3, 7), (4, 4), (5, 9), (6, 9), (7, 8), (8, 3), (9, 2), (12, 1), (13, 8), (16, 3), (19, 9), (21, 1), (22, 5), (24, 6), (26, 7), (30, 9), (36, 4), (37, 6), (38, 1), (39, 9), (41, 8), (42, 7), (43, 4), (49, 5)],
    34: [(1, 1), (2, 9), (5, 1), (6, 2), (7, 2), (8, 1), (12, 7), (15, 6), (16, 10), (19, 6), (20, 6), (21, 2), (24, 5), (25, 5), (27, 8), (31, 1), (36, 1), (40, 3), (42, 2), (44, 3), (45, 8), (46, 8)],
    35: [(0, 1), (1, 9), (2, 6), (3, 9), (5, 8), (9, 4), (12, 7), (13, 6), (14, 1), (16, 6), (17, 9), (18, 10), (22, 8), (23, 2), (24, 6), (28, 3), (31, 3), (32, 9), (36, 1), (39, 1), (40, 4), (41, 6), (42, 5), (43, 3), (44, 2)],
    36: [(0, 2), (1, 7), (3, 3), (4, 10), (7, 1), (8, 7), (9, 1), (11, 6), (13, 1), (15, 8), (16, 3), (19, 6), (20, 5), (21, 10), (26, 7), (32, 7), (33, 4), (34, 1), (35, 1), (39, 5), (40, 9), (41, 2), (43, 9), (44, 3), (45, 2), (47, 3), (49, 10)],
    37: [(3, 2), (5, 10), (9, 5), (12, 9), (21, 6), (24, 3), (26, 9), (27, 3), (28, 7), (29, 3), (31, 6), (32, 4), (33, 6), (38, 6), (41, 4), (42, 6), (43, 9), (47, 2)],
    38: [(2, 2), (3, 4), (4, 8), (6, 8), (7, 8), (12, 10), (13, 2), (14, 4), (19, 7), (22, 4), (26, 4), (28, 2), (31, 6), (32, 1), (33, 1), (37, 6), (40, 4), (41, 6), (42, 5), (43, 2), (45, 2), (49, 3)],
    39: [(0, 7), (4, 3), (7, 1), (8, 6), (9, 4), (16, 4), (18, 9), (19, 4), (20, 5), (22, 1), (24, 9), (26, 3), (27, 4), (29, 2), (31, 5), (33, 9), (35, 1), (36, 5), (42, 2), (43, 6), (45, 6), (46, 8), (48, 8), (49, 7)],
    40: [(5, 4), (7, 2), (8, 4), (9, 2), (12, 9), (13, 5), (16, 2), (17, 10), (18, 5), (20, 5), (21, 7), (22, 1), (23, 6), (24, 2), (25, 9), (26, 7), (28, 6), (29, 1), (30, 3), (34, 3), (35, 4), (36, 9), (38, 4), (41, 4), (42, 1), (44, 2), (45, 6), (47, 4), (48, 3)],
    41: [(1, 1), (2, 1), (3, 6), (6, 7), (7, 6), (11, 1), (13, 7), (15, 9), (16, 1), (18, 8), (21, 4), (23, 6), (29, 3), (30, 6), (31, 7), (33, 8), (35, 6), (36, 2), (37, 4), (38, 6), (40, 4), (42, 10), (46, 1), (47, 9), (49, 7)],
    42: [(3, 2), (6, 9), (8, 4), (13, 3), (15, 8), (17, 9), (20, 8), (21, 1), (22, 10), (23, 2), (26, 9), (28, 8), (32, 2), (33, 7), (34, 2), (35, 5), (37, 6), (38, 5), (39, 2), (40, 1), (41, 10), (44, 1), (45, 7), (47, 10), (48, 4)],
    43: [(3, 2), (6, 7), (7, 5), (8, 5), (10, 8), (11, 9), (15, 10), (23, 9), (25, 4), (27, 3), (29, 6), (30, 4), (31, 5), (33, 4), (35, 3), (36, 9), (37, 9), (38, 2), (39, 6)],
    44: [(1, 6), (2, 4), (3, 10), (5, 10), (7, 3), (8, 10), (9, 2), (13, 1), (14, 8), (16, 7), (17, 5), (19, 4), (21, 1), (22, 7), (23, 3), (26, 2), (28, 8), (30, 3), (31, 10), (34, 3), (35, 2), (36, 3), (40, 2), (42, 1), (49, 10)],
    45: [(0, 6), (1, 6), (7, 8), (8, 4), (9, 6), (11, 1), (12, 10), (13, 4), (15, 5), (17, 2), (19, 2), (20, 8), (21, 2), (22, 9), (23, 1), (24, 10), (25, 2), (29, 6), (31, 7), (34, 8), (36, 2), (38, 2), (39, 6), (40, 6), (42, 7), (46, 3), (47, 3)],
    46: [(0, 7), (1, 10), (2, 2), (3, 7), (4, 10), (7, 2), (8, 10), (9, 8), (14, 7), (16, 2), (17, 10), (19, 6), (21, 3), (25, 7), (27, 4), (34, 8), (39, 8), (41, 1), (45, 3), (47, 2)],
    47: [(0, 2), (6, 7), (8, 8), (10, 2), (12, 5), (16, 4), (18, 9), (19, 7), (21, 9), (22, 10), (23, 9), (24, 9), (25, 6), (26, 4), (27, 1), (28, 9), (29, 10), (31, 7), (32, 7), (36, 3), (37, 2), (40, 4), (41, 9), (42, 10), (45, 3), (46, 2), (48, 4)],
    48: [(1, 3), (2, 3), (3, 2), (5, 7), (6, 10), (9, 7), (10, 6), (15, 1), (16, 8), (18, 8), (19, 10), (22, 10), (23, 10), (26, 2), (29, 1), (39, 8), (40, 3), (42, 4), (47, 4), (49, 3)],
    49: [(1, 8), (3, 10), (4, 6), (9, 9), (11, 7), (14, 1), (16, 6), (21, 4), (22, 7), (23, 8), (25, 6), (27, 6), (28, 10), (31, 8), (32, 6), (33, 5), (36, 10), (38, 3), (39, 7), (41, 7), (44, 10), (48, 3)],
}

grafo = gr.Grafo(grafica)

for g in grafica:
    for x in grafica:
        if g == x:
            continue

        path = grafo.a_estrella(g,x)
        print('El camino mas corto de ',g,' a ',x,' es: ',path[0], 'con costo: ', path[1])