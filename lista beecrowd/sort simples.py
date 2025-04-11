n1 = float(input())
n2 = float(input())
n3 = float(input())

orig1 = n1
orig2 = n2
orig3 = n3

valores = [n1 , n2 , n3] #aqui os números estão em listas 
valores.sort() #o .sort vai deixar os números em ordem crescrente 

for v in valores:
    print("{}".format(v))

print()

print(orig1)
print(orig2)
print(orig3)
