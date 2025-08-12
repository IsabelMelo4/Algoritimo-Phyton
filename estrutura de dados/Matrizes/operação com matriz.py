# soma de matriz 

linha, coluna = map(int, input().split())
linha2, coluna2 = map(int, input().split())

matriz1 = [[0 for _ in range(coluna)] for _ in range(linha)]
matriz2 = [[0 for _ in range(coluna2)] for _ in range(linha2)]

for l in range(linha):
    for c in range(coluna):
        matriz1[l][c] = int(input(f"digite um valor na posição {l}x{c} matriz 1: "))

for linha in range(linha2):
    for coluna in range(coluna2):
        matriz2[linha][coluna] = int(input(f"digite um valor na posição {linha}x {coluna} matriz 2: "))

for linha in matriz1:
    print (linha)
for linha in matriz2:
    print(linha)
