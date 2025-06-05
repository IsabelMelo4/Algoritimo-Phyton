cont = 0 

for c in range (1, 7):
    valor = float(input())
    if valor > 0:
        cont += 1      #se a condição for verdadeira, o contador aumenta 1 tipo
                       #primeiro numero é par? aumenta 1 segundo é par? aumenta outro e assim vai 

print(f"{cont} valores positivos")


