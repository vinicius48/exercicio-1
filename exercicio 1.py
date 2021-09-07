matriz_A = [[0,1,0], [1,0,0], [0,0,1]]
matriz_E = [[0,0,0], [0,0,0], [0,0,0]]
matriz_B = [[1,1,1], [0,2,3], [5,5,1]]
matriz_oposta_B = [[0,0,0], [0,0,0], [0,0,0]]
matriz_C = [[1,-2,-3], [0,-4,4], [0,0,0]]
matriz_oposta_C = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(3):
    for c in range(3):
        matriz_E[l][c]=matriz_A[l][c]-matriz_A[l][c]*2
        matriz_oposta_B[l][c]=matriz_B[l][c]-matriz_B[l][c]*2
        matriz_oposta_C[l][c]=matriz_C[l][c]-matriz_C[l][c]*2
print(f'matriz oposta de A ( {matriz_E} )')
print(f'matriz oposta de B ( {matriz_oposta_B} )')
print(f'matriz oposta de C ( {matriz_oposta_C} )')


