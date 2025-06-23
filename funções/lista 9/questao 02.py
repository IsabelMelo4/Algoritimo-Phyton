#criar uma funcao par ou impar 

def impar_ou_par(n):
    if n %2 != 0:

        print("é impar")

    elif n %2 == 0:
        print("é par")

#progama principal

num = int(input("Digite um numero:"))

impar_ou_par(num)

