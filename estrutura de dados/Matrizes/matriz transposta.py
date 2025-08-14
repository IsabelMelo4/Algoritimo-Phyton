linhaM, colunaM = map(int, input().split())

matriz = [[0 for _ in range(colunaM)] for _ in range(linhaM)]


for i in range(linhaM):
    for j in range(colunaM):
        matriz[i][j] = int(input("valores"))

transposta = [[matriz[j][i] for j in range(linhaM)] for i in range(colunaM)]

print("normal")

print(" ")
for linha in matriz:
    print(linha)

print(" ")

print("transposta")
print(" ")
for linha in transposta:
    print(linha)


# soma 

if linhaM == colunaM:

    soma = [[0 for _ in range(linhaM)] for _ in range(colunaM)]

    for i in range(linhaM):
        for j in range(colunaM):
            soma[i][j] = transposta[i][j] + matriz[i][j]

   
        print("SOMA")
        print(" ")
        for linha in soma:
            print(linha)
else: 
    print("NAO E POSSIVEL SOMAR AS MATRIZES")



#multiplicação 

if len(transposta[0]) == len(matriz):
    
    resultado = [[0 for _ in range(colunaM)] for _ in range(colunaM)]

    for i in range(colunaM):
        for j in range(colunaM):
            for k in range(linhaM):
                resultado[i][j] += transposta[i][k] * matriz[k][j]

print("multiplicação")
print(" ")

for linha in resultado:
    print(linha)

    