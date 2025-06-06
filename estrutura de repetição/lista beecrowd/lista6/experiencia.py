Qtestes = int(input())
total = 0
coelhos = 0
ratos = 0 
sapos = 0 


for i in range(Qtestes):
    quant, tipo =  input().split()
    quant = int(quant)
     
    if tipo == "C":
       coelhos += quant 
    elif tipo == "R":
       ratos += quant 
    elif tipo == "S":
       sapos += quant 

total = coelhos + ratos + sapos
percentualR = (ratos / total) * 100
percentualC = (coelhos / total) * 100
percentualS = (sapos / total) * 100

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos)) 
print("Total de ratos: {}".format(ratos)) 
print("Total de sapos: {}".format(sapos)) 
print("Percentual de coelhos: {:.2f} %".format(percentualC))
print("Percentual de ratos: {:.2f} %".format(percentualR))
print("Percentual de sapos: {:.2f} %".format(percentualS))