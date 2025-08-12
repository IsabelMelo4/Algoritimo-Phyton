                       # soma de matrizes 


# Só é possível somar e subtrair matrizes com mesmo número de linhas e colunas.

a = [[1, 2],
     [3, 4]]

b =  [[5, 6],
      [7, 8]]

soma = [[0 for _ in range(2)] for _ in range(2)]
subtração = [[0 for _ in range(2)]for _ in range(2)]

for l in range(2):
    for j in range(2):
        soma[l][j] = a[l][j] + b[l][j]
        subtração[l][j] = a[l][j] - b[l][j]

print(soma)
print(subtração)



#  o número de colunas da matriz A deve ser igual ao número de linhas da matriz B para que a multiplicação seja possível.

linha1, coluna1 = map(int, input().split())
linha2, coluna2 = map(int, input().split())

if coluna1 != linha2:
    print("não é possivel multiplicar")

else:
    matriz1 = [[3 for _ in range(coluna1)] for _ in range(linha1)]
    matriz2 = [[3 for _ in range(coluna2)] for _ in range(linha2)]

    resultado = [[0 for _ in range(coluna2)] for _ in range(linha1)]

    for l1 in range(linha1):
        for c2 in range(coluna2):
            for k in range(coluna1):
                resultado[l1][c2] = matriz1[l1][k] * matriz2[k][c2]

    for lin in resultado:
         print(lin)

