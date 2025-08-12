# Passo 1: Ler as dimensões da primeira matriz
# map(int, input().split()) → lê dois números separados por espaço e converte para int
linha, coluna = map(int, input().split())

# Passo 2: Ler as dimensões da segunda matriz
linha2, coluna2 = map(int, input().split())

# Passo 3: Criar a estrutura das matrizes já com zeros
# [[0 for _ in range(coluna)] for _ in range(linha)] → cria lista de listas com zeros

matriz1 = [[0 for _ in range(coluna)] for _ in range(linha)]
matriz2 = [[0 for _ in range(coluna2)] for _ in range(linha2)]
print(matriz1)
print(matriz2)

# Passo 4: Preencher a primeira matriz
# Dois loops (linhas e colunas) percorrem cada posição e pedem um valor

for l in range(linha):
    for c in range(coluna):
        matriz1[l][c] = int(input(f"digite um valor na posição {l}x{c} matriz 1: "))

# Passo 5: Preencher a segunda matriz (mesmo processo)

for l2 in range(linha2):
    for c2 in range(coluna2):
        matriz2[l2][c2] = int(input(f"digite um valor na posição {l2}x{c2} matriz 2: "))

# Passo 6: Mostrar as matrizes na tela
# Aqui, cada item de matriz1/matriz2 é uma lista que representa uma linha
# for linha in matriz1: print(linha) → imprime uma linha por vez

for linha in matriz1:
    print(linha)

for linha in matriz2:
    print(linha)

"""
Resumo de como montar uma matriz:
1. Ler o número de linhas e colunas.
2. Criar uma lista de listas inicializada com zeros.
3. Percorrer com dois loops (for aninhados) e preencher cada posição com um valor.
4. Imprimir percorrendo linha por linha.
Obs.: índice [i][j] significa: linha i, coluna j (começando do 0).
"""
