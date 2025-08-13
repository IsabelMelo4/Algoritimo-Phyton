# #Escreva um algoritmo que leia 30 n ́umeros inteiros e os armazene em uma lista. Escreva as
# funçoes maior, menor e soma. Elas devem receber a lista e retornar o respectivo valor. Por
# fim, fa ̧ca chamadas `as fun ̧c ̃oes e imprima os retornos
def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def soma(lista):
    return sum(lista)

numero = []


for i in range(10):
    num = int(input())
    numero.append(num)

print("maior numero", maior(numero))
print("menor numero", menor(numero))
print("soma", soma(numero))