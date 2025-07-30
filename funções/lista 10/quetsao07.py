#7. Escreva uma função recursiva que receba 2 inteiros positivos, n e d, onde necessariamente o
#inteiro d possua apenas 1 digito. A função deve retornar o número de ocorrências de d em n.

def contaDigito(n,d):
    if n < 10:
        return int(n == d)
    if n % 10 == d:
        return 1 + contaDigito(n//10, d)
    else:
        return contaDigito(n//10, d)
    

nn = int(input())
dd = int(input())

print(contaDigito(nn, dd))

 