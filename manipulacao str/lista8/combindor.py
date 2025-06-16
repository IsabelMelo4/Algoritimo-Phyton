teste = int(input())

for n in range(teste):
    texto1, texto2 = input().split()
    resultado = []

    tamanho = max(len(texto1), len(texto2))

    for i in range(tamanho):
        if i < len(texto1):
            resultado.append(texto1[i])
        if i < len(texto2):
            resultado.append(texto2[i])
    
    print("".join(resultado))
    


