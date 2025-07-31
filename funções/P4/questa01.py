def contarVogais(texto):

    cont = 0 
    for c in texto:
        if c in "AEIOU":
            cont += 1
    return cont


print(contarVogais("ProgAmAr É divertido"))


