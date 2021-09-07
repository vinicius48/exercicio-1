matriz_a = [[3,4], [2,3]]
matriz_x = [[0,0], [0,0]]
for[l] in range[2]:
    for[c] in range[2]:
     matriz_a[l][c] = matriz_a[l][c] * matriz_x[l][c]
    matriz_x[l][c] = matriz_a[l][c] * 1/1

print(matriz_x, '\n', matriz_a)
