matriz = [] # vai criar uma lista vazia sem nada 

for i in range(2): #vai repetir 3 vezes a lista linha 
    linha = []
    for j in range(2): # a cade tres vezes(tres colunas) ele vai pedir um numero
        valor = int(input()) # vai ler o numero 
        linha.append(valor) # vai colocar dentro da linha 
    matriz.append(linha) # e vai adicionar a linha na matriz 

print(matriz)

# primeira repetição

# linha = vazia                                              linha[]
# primeira coluna( for j)                          
# vai ler um valor 
#vai adicionar esse valor na primeira colona da linha        linha[1]
# vai ler outro valor                                       
#vai adicionar esse valor na segunda coluna da linha         linha[1][2]
# vai ler esse valor 
# vai adiconar na terceira coluna da linha                   linha[1][2] [3] 
# adiciona a linha a matriz                                  matriz[linha[1][2][3]]

# segunda repetição

# linha vazia 

# primeira coluna( for j) 
# vai ler um valor 
#vai adicionar esse valor na primeira colona da linha
# vai ler outro valor 
#vai adicionar esse valor na segunda coluna da linha 
# vai ler esse valor 
# vai adiconar na terceira coluna da linha 
# adiciona a linha a matriz 

# terceira repetição

# primeira coluna( for j) 
# vai ler um valor 
#vai adicionar esse valor na primeira colona da linha
# vai ler outro valor 
#vai adicionar esse valor na segunda coluna da linha 
# vai ler esse valor 
# vai adiconar na terceira coluna da linha 
# adiciona a linha a matriz 


#exibir a matriz 

for i in range(2): # primeira linha ele cai em tres repetições
    for j in range(2): # e nessas tres repeticoes
        print(matriz[i][j], end=" ") # ele exibe o elemento na casa repetição 1 (linha 1) e o elemento da coluna (j 1, 2 ,3),
    print()

