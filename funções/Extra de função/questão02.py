def inverter_palavra(frase):
    saida = ""

    palavras = frase.split()

    for palavra in palavras:
   
        saida += palavra[::-1] + " "
   
    
    return saida.strip()

# Testando a função
print(inverter_palavra("Python é divertido"))