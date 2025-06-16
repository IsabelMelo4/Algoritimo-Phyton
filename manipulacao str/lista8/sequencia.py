import sys

for frase in sys.stdin:
    maiusculo = False
    novotexto = ""

    for pos, letra in enumerate(frase):
        
        if (pos == 0 and letra.isalpha()) or letra.isalpha() and maiusculo == False :
            novotexto += letra.upper()
            maiusculo = not maiusculo

        elif letra.isalpha() and maiusculo == True:
             novotexto += letra.lower()
             maiusculo = not maiusculo

        else:
             novotexto += letra

    print(novotexto, end="") 