texto = input()
novoTexto = ""

italico_aberto = False
negrito_aberto = False

for caractere in texto:
    if caractere == "_":
        novoTexto += "</i>" if italico_aberto else "<i>"
        italico_aberto = not italico_aberto
    elif caractere == "*":
        novoTexto += "</b>" if negrito_aberto else "<b>"
        negrito_aberto = not negrito_aberto
    else:
        novoTexto += caractere

print(novoTexto)


