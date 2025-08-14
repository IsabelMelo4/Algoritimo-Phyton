linha1, coluna1 = map(int, input().split())
linha2, coluna2 = map(int, input().split())

if linha1 != coluna2:
    print("não é possivel multiplicar")

else:
    matriz1 = [[0 for _ in range(linha1)] for _ in range(coluna1)]
    matriz2 = [[0 for _ in range(coluna2)] for _ in range(linha2)]
    resultado = [[0 for _ in range(coluna2)] for _ in range(linha1)]

    for l1 in range(linha1):
        for c1 in range(coluna1):
            matriz1[l1][c1] = int(input("matriz 1"))

    for l2 in range(linha2):
        for c2 in range(coluna2):
            matriz2[l2][c2] = int(input("matriz 2:"))

    for i in range(linha1):
        for j in range(coluna2):
            for k in range(coluna1):
                resultado[i][j] = matriz1[i][k] * matriz2[j][k]

    print(matriz1)
    print(matriz2)

    for linha in resultado:
        print(linha)


