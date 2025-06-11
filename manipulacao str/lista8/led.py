testes = int(input())

for n in range(testes):
    numeros = input()
    
    soma = 0
    
    for i in numeros:
        if i == "0":
            soma += 6
 
        elif i == "1":
            soma += 2

        elif i == "2":
            soma += 5

        elif i == "3":
            soma += 5

        elif i == "4":
            soma += 4

        elif i == " 5":
            soma += 5

        elif i == "6":
            soma += 6

        elif i == "7":
            soma += 3

        elif i == "8":
            soma += 7

        elif i == "9":
           soma += 6

print("{} leds".format(soma))    
