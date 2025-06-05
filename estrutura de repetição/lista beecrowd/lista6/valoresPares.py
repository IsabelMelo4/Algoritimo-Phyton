contador = 0

for c in range (1, 5):
    num = int(input())
    if num % 2 != 0:
        contador += 1

print("{} valores pares".format(contador))