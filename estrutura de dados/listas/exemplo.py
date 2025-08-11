                        #listas
#declaração de lista 

lanche = ["hamburger ", "suco", "pizza", "pudim"]
print(lanche)
print(lanche[3]) #printa o exercicio na casa 3 
#modificar lista

lanche[3] = "novo elemento"

#Adicionar elementos a lista 

lanche.append("cookie") #adiciona item no final da lista
lanche.insert(0, "cachorro quente") #adiciona intem em uma posição especifica

#apagar elementos 

del lanche[3]#apaga o elemento da casa
lanche.pop()#elimina o ultimo ou o parametro que vc passar 
lanche.remove("pizza") # remove o conteudo especifico e seu indice 

#ordenar lista 

lanche.sort()


