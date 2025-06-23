# criar uma funcao que some dois numeros 

def soma(n1, n2):
    return n1 + n2

def linha():
    print("-"*30)

#progama principal
linha()
print("progama de somas")
linha()

n1, n2 = map(int, input("digite dois numeros:").split())

linha()

resultado = soma(n1, n2)
print("Resultado: {}".format(resultado))

linha()


