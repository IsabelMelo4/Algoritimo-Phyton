def remover_vogais(texto):

    if texto == "":
        return ""
    
    if texto[0] in "aeiouy ":
        # Se for vogal ou espaço, chama recursivamente para o resto da string
        return remover_vogais(texto[1:])
    else:
        # Se não for vogal ou espaço, mantém o caractere e chama recursivamente
        return texto[0] + remover_vogais(texto[1:])

# Testando a função
print(remover_vogais("Python e legal"))  # Saída: "Pthnlg"   

