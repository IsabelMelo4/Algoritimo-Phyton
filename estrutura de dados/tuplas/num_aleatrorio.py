#gerar numero aleatorio e colocar na tupla e dizer quem foi o maior e quem foi o menor 
from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(tupla)
print(max(tupla))
print(min(tupla))