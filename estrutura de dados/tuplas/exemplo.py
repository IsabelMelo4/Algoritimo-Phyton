lanche = ("hambuguer", "suco", "pizza", "pudim", "batata frita")

#tuplas são imutavéis, elas não podem se alterar nem modificar os elementos

                            #fatiamento


print(lanche[3]) #mostra o lanche no espaço 3
print(lanche[-3]) #mostra o lanche de trás pra frente 
print(lanche[2:]) #mostra o lanche apartir do 2
print(lanche[:3]) #mostra o lanche do começo menos o 3

                                
                                #loops com tuplas

for comida in lanche:
    print("Eu vou comer {}".format(comida))

print("Comi pra caramba ")


for pos, comida in enumerate(lanche): #aqui ele coloca a posição da lista COM O ENUMERATE
    print("Eu vou comer {} {}".format(comida, pos))


                                    # ordenar tupla
a = (1, 2, 5, 3 ,7,10,4,6)
print(a)
print(sorted(a))

                                 #endereçamento de tupla

print(a.count(3)) #count vai mostrar quantas vezes aparece tal elemento
print(a.index(5)) #index mostra a posição que o 5 está 
print(a.index(5, 2)) #mostrar a ocorrencia apartir de uma posição, primeiro o numero depois a posição 





