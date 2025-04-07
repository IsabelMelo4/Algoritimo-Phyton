#entrada
valor = int(input())

#processamento
notas100 = valor // 100 
valor %= 100 

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20 

notas10 = valor // 10
valor %= 10

notas5 = valor // 5 
valor %= 5

notas2 = valor // 2 
valor %= 2 

notas1 = valor

print(f"{notas100}Nota(s) de R$ 100")
print(f"{notas50}Nota(s) de R$ 50")
print(f"{notas20}Nota(s) de R$ 20")
print(f"{notas10}Nota(s) de R$ 10")
print(f"{notas5}Nota(s) de R$ 5")
print(f"{notas2}Nota(s) de R$ 2")
print(f"{notas1}Nota(s) de R$ 1")




