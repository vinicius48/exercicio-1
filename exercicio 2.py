matriz_a = [[1,2], [4,-1]]
matriz_oposta_a = [[0,0], [0,0]]
matriz_b = [[0,0], [0,0]]

for l in range(2):
    for c in range(2):
        matriz_oposta_a[l][c] = matriz_a[l][c] - matriz_a[l][c] * 2
        matriz_b[l][c] = matriz_a[l][c] * (1/9)

print(matriz_b, '\n', matriz_oposta_a)
assert matriz_b != matriz_oposta_a

