
valor = []

for i in range(10):
    Valor_digitado = int(input())

    valor.append(Valor_digitado)

for pos, digito in enumerate(valor):
    if digito <= 0:
        digito = 1
   
    print("X[{}] = {}".format(pos, digito))


   
