#2. Escreva uma função recursiva em Python que receba o primeiro termo (a1), a razão e o
#número de elementos, n, de uma Progressão Aritmética (PA) e, em seguida, calcule e retorne
#o resultado da soma dos termos da PA.

def pA(a1, r,n):
    if n == 1:
        return 1 
    
    return a1 + pA(a1 + r, r, n-1)

#linha de resursão: ele vai retornar a função com novos parametros 
#a1 é uma variável (provavelmente um número ou um valor que foi passado como argumento para a função onde essa linha de código está).

#r também é uma variável, provavelmente um número.

#A função pA é chamada com três parâmetros: a1 + r, r, e a1 - 1.

#Depois que a função pA(a1 + r, r, a1 - 1) for executada e retornar um valor, esse valor será somado a a1. A operação final é então a soma de a1 com o retorno da função pA.


print(pA(45,8,10))


# Passo a Passo da Execução:

# Primeira chamada: pA(45, 8, 10)

# n = 10, então a função não entra no caso base.

# Chama a recursão: a1 + pA(a1 + r, r, n-1) → 45 + pA(53, 8, 9)

# Segunda chamada: pA(53, 8, 9)

# n = 9, então a função não entra no caso base.

# Chama a recursão: 53 + pA(61, 8, 8)

# Terceira chamada: pA(61, 8, 8)

# n = 8, então a função não entra no caso base.

# Chama a recursão: 61 + pA(69, 8, 7)

# Quarta chamada: pA(69, 8, 7)

# n = 7, então a função não entra no caso base.

# Chama a recursão: 69 + pA(77, 8, 6)

# Quinta chamada: pA(77, 8, 6)

# n = 6, então a função não entra no caso base.

# Chama a recursão: 77 + pA(85, 8, 5)

# Sexta chamada: pA(85, 8, 5)

# n = 5, então a função não entra no caso base.

# Chama a recursão: 85 + pA(93, 8, 4)

# Sétima chamada: pA(93, 8, 4)

# n = 4, então a função não entra no caso base.

# Chama a recursão: 93 + pA(101, 8, 3)

# Oitava chamada: pA(101, 8, 3)

# n = 3, então a função não entra no caso base.

# Chama a recursão: 101 + pA(109, 8, 2)

# Nona chamada: pA(109, 8, 2)

# n = 2, então a função não entra no caso base.

# Chama a recursão: 109 + pA(117, 8, 1)

# Décima chamada: pA(117, 8, 1)

# n = 1, então entra no caso base e retorna 1.





#Desempilhamento da Recursão:

# Agora, as chamadas começam a retornar, e os valores são somados:

# Décima chamada retorna: 1

# Nona chamada retorna: 109 + 1 = 110

# Oitava chamada retorna: 101 + 110 = 211

# Sétima chamada retorna: 93 + 211 = 304

# Sexta chamada retorna: 85 + 304 = 389

# Quinta chamada retorna: 77 + 389 = 466

# Quarta chamada retorna: 69 + 466 = 535

# Terceira chamada retorna: 61 + 535 = 596

# Segunda chamada retorna: 53 + 596 = 649

# Primeira chamada retorna: 45 + 649 = 694