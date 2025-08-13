# 3. Escreva um algoritmo que imprima a lista dos 100 primeiros n ́umeros primos, iniciando do
# 2. N ́umero primo  ́e um n ́umero natural que tem apenas dois divisores diferentes, o 1 e ele
# mesmo. Por defini ̧c ̃ao, 1 n ̃ao e primo. Crie e utilize uma fun ̧c ̃ao que indica se um n ́umero
# e primo ou n ̃ao e mantenha os n ́umeros primos em uma lista. Imprima, ao final, a soma
# dos 100 n ́umeros primos impressos. Para isso, crie uma fun ̧c ̃ao chamada soma que receba
# a lista como parˆametro e retorne a soma.


def e_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    
def gerar_primos(cont):
     primos  = []
     num_primo = 2
     while len(primos) < cont:
        if e_primo(num_primo):
            primos.append(num_primo)
        num_primo += 1
     return primos

def soma(lista):
    return sum(lista)

contador = 10

primos = gerar_primos(contador)
contador = gerar_primos(contador)
print(gerar_primos(primos))



