contPar = 0
contImp = 0
contPOs= 0
contNeg = 0

for c in range (0,5):
    num = int(input())
    if num % 2 == 0:
        contPar += 1 
    if num % 2 != 0:
         contImp += 1 
    if num > 0:
         contPOs += 1
    if num < 0:
         contNeg += 1

print(f"{contPar} valor(es) par(es)")
print(f"{contImp} valor(es) impar(es)")
print(f"{contPOs} valor(es) positivos(s)")
print(f"{contNeg} valor(es) negativos(s)")

