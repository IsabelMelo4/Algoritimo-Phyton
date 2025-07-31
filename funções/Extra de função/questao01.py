def contar_vogais_minusculas(frase):
    vogais = "aeiou"
    cont = 0
    
    for letra in frase:
        if letra in vogais: # in verifica se está dentro
            cont += 1
    return cont

print(contar_vogais_minusculas("Estudar é muito bom"))